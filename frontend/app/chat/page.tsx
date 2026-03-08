"use client";

import { useState, useRef, useEffect } from "react";
import { ChatMessage } from "@/types/chat";
import { API_BASE } from "@/lib/api";
import ReactMarkdown from "react-markdown";

const suggestions = [
  "Best laptop for programming under $1500",
  "Gaming laptop with good battery life",
  "Lightest ultrabook for travel",
  "Best laptop for video editing",
  "Compare MacBook Pro vs Dell XPS",
  "Student laptop under $800",
];

export default function ChatPage() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [isStreaming, setIsStreaming] = useState(false);
  const [sessionId, setSessionId] = useState<string | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  async function sendMessage(text: string) {
    if (!text.trim() || isStreaming) return;

    const userMessage: ChatMessage = { role: "user", content: text };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsStreaming(true);

    const assistantMessage: ChatMessage = { role: "assistant", content: "" };
    setMessages((prev) => [...prev, assistantMessage]);

    try {
      const response = await fetch(`${API_BASE}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          message: text,
          session_id: sessionId,
          conversation_history: messages.map((m) => ({ role: m.role, content: m.content })),
        }),
      });

      const reader = response.body?.getReader();
      const decoder = new TextDecoder();

      if (!reader) return;

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value, { stream: true });
        const lines = chunk.split("\n");

        for (const line of lines) {
          if (!line.startsWith("data: ")) continue;
          try {
            const data = JSON.parse(line.slice(6));
            if (data.type === "token") {
              setMessages((prev) => {
                const updated = [...prev];
                const last = updated[updated.length - 1];
                if (last.role === "assistant") {
                  last.content += data.content;
                }
                return [...updated];
              });
            } else if (data.type === "session") {
              setSessionId(data.session_id);
            }
          } catch {
            // skip malformed JSON
          }
        }
      }
    } catch (error) {
      setMessages((prev) => {
        const updated = [...prev];
        const last = updated[updated.length - 1];
        if (last.role === "assistant") {
          last.content = "Sorry, something went wrong. Please try again.";
        }
        return [...updated];
      });
    }

    setIsStreaming(false);
  }

  return (
    <div className="max-w-4xl mx-auto px-4 h-[calc(100vh-4rem)] flex flex-col">
      {/* Messages */}
      <div className="flex-1 overflow-y-auto py-6 space-y-6 scrollbar-hide">
        {messages.length === 0 && (
          <div className="flex flex-col items-center justify-center h-full">
            <h2 className="text-2xl font-bold mb-2">
              <span className="text-[var(--accent)]">Laptop</span>Finder AI
            </h2>
            <p className="text-[var(--muted)] mb-8">Ask me anything about laptops</p>
            <div className="grid grid-cols-2 gap-3 max-w-lg">
              {suggestions.map((s) => (
                <button
                  key={s}
                  onClick={() => sendMessage(s)}
                  className="text-left text-sm p-3 rounded-lg border border-[var(--border)] bg-[var(--card)] hover:border-[var(--accent)] transition-colors"
                >
                  {s}
                </button>
              ))}
            </div>
          </div>
        )}

        {messages.map((msg, i) => (
          <div key={i} className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}>
            <div
              className={`max-w-[80%] rounded-2xl px-4 py-3 ${
                msg.role === "user"
                  ? "bg-[var(--accent)] text-black"
                  : "bg-[var(--card)] border border-[var(--border)]"
              }`}
            >
              {msg.role === "assistant" ? (
                <div className="prose prose-invert prose-sm max-w-none">
                  <ReactMarkdown>{msg.content || "..."}</ReactMarkdown>
                </div>
              ) : (
                <p className="text-sm">{msg.content}</p>
              )}
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="py-4 border-t border-[var(--border)]">
        <div className="flex gap-3">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage(input)}
            placeholder="Ask about laptops..."
            disabled={isStreaming}
            className="flex-1 px-4 py-3 rounded-xl bg-[var(--card)] border border-[var(--border)] focus:border-[var(--accent)] focus:outline-none disabled:opacity-50"
          />
          <button
            onClick={() => sendMessage(input)}
            disabled={isStreaming || !input.trim()}
            className="px-6 py-3 bg-[var(--accent)] text-black font-semibold rounded-xl hover:opacity-90 disabled:opacity-50"
          >
            {isStreaming ? "..." : "Send"}
          </button>
        </div>
      </div>
    </div>
  );
}
