from collections.abc import AsyncGenerator
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.chat_repo import ChatRepository
from app.rag.retriever import retrieve_relevant_laptops
from app.rag.generator import generate_response


class ChatService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.chat_repo = ChatRepository(db)

    async def chat(
        self,
        message: str,
        session_id: UUID | None = None,
        conversation_history: list[dict] | None = None,
    ) -> AsyncGenerator[str, None]:
        try:
            if not session_id:
                session = await self.chat_repo.create_session(title=message[:100])
                session_id = session.id

            await self.chat_repo.add_message(session_id, "user", message)

            yield f"data: {{\"type\": \"session\", \"session_id\": \"{session_id}\"}}\n\n"

            price_max = self._extract_budget(message)
            chunks = await retrieve_relevant_laptops(
                query=message, db=self.db, price_max=price_max
            )

            laptop_ids = list(set(c["laptop_id"] for c in chunks))

            full_response = []

            async for token in generate_response(
                query=message,
                context_chunks=chunks,
                conversation_history=conversation_history,
            ):
                full_response.append(token)
                escaped = token.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
                yield f"data: {{\"type\": \"token\", \"content\": \"{escaped}\"}}\n\n"

            sources = [{"laptop_id": c["laptop_id"], "similarity": c["similarity"], "chunk_type": c["chunk_type"]} for c in chunks[:5]]
            await self.chat_repo.add_message(
                session_id, "assistant", "".join(full_response),
                recommended_laptop_ids=laptop_ids, sources=sources,
            )

            yield f"data: {{\"type\": \"done\", \"laptop_ids\": {laptop_ids}}}\n\n"
        except Exception as e:
            import logging
            logging.exception("Chat error")
            yield f"data: {{\"type\": \"error\", \"content\": \"Something went wrong: {str(e)[:200]}\"}}\n\n"

    def _extract_budget(self, message: str) -> float | None:
        import re
        patterns = [
            r"under\s*\$?([\d,]+)",
            r"below\s*\$?([\d,]+)",
            r"budget.*\$?([\d,]+)",
            r"less than\s*\$?([\d,]+)",
            r"\$?([\d,]+)\s*or less",
            r"max.*\$?([\d,]+)",
        ]
        for pattern in patterns:
            match = re.search(pattern, message.lower())
            if match:
                return float(match.group(1).replace(",", ""))
        return None
