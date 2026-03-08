export interface ChatMessage {
  id?: string;
  role: "user" | "assistant";
  content: string;
}

export interface StreamEvent {
  type: "session" | "token" | "done";
  content?: string;
  session_id?: string;
  laptop_ids?: string[];
}
