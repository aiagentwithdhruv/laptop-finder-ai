from collections.abc import AsyncGenerator

from openai import AsyncOpenAI

from app.config import get_settings
from app.rag.prompts import SYSTEM_PROMPT, CONTEXT_TEMPLATE

settings = get_settings()
client = AsyncOpenAI(api_key=settings.openai_api_key)


async def generate_response(
    query: str,
    context_chunks: list[dict],
    conversation_history: list[dict] | None = None,
) -> AsyncGenerator[str, None]:
    context = "\n\n---\n\n".join(chunk["content"] for chunk in context_chunks)
    user_message = CONTEXT_TEMPLATE.format(context=context, query=query)

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    if conversation_history:
        for msg in conversation_history[-10:]:
            messages.append({"role": msg["role"], "content": msg["content"]})

    messages.append({"role": "user", "content": user_message})

    stream = await client.chat.completions.create(
        model=settings.llm_model,
        max_tokens=2048,
        messages=messages,
        stream=True,
    )

    async for chunk in stream:
        delta = chunk.choices[0].delta
        if delta.content:
            yield delta.content
