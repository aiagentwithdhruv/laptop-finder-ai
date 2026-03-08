import Link from "next/link";

const categories = [
  { name: "Ultrabook", emoji: "💻", slug: "ultrabook" },
  { name: "Gaming", emoji: "🎮", slug: "gaming" },
  { name: "Workstation", emoji: "⚡", slug: "workstation" },
  { name: "Business", emoji: "💼", slug: "business" },
  { name: "Budget", emoji: "💰", slug: "budget" },
  { name: "2-in-1", emoji: "🔄", slug: "2in1" },
];

export default function HomePage() {
  return (
    <div className="max-w-7xl mx-auto px-4 py-20">
      {/* Hero */}
      <div className="text-center mb-20">
        <h1 className="text-5xl font-bold mb-6">
          Find Your Perfect{" "}
          <span className="text-[var(--accent)]">Laptop</span>
        </h1>
        <p className="text-xl text-[var(--muted)] mb-10 max-w-2xl mx-auto">
          AI-powered recommendations based on your needs. Browse, compare, and chat with our AI to find the laptop that fits you.
        </p>
        <div className="flex gap-4 justify-center">
          <Link
            href="/chat"
            className="px-8 py-3 bg-[var(--accent)] text-black font-semibold rounded-lg hover:opacity-90 transition-opacity"
          >
            Ask AI for Recommendations
          </Link>
          <Link
            href="/laptops"
            className="px-8 py-3 border border-[var(--border)] rounded-lg hover:border-[var(--accent)] transition-colors"
          >
            Browse All Laptops
          </Link>
        </div>
      </div>

      {/* Categories */}
      <div className="mb-20">
        <h2 className="text-2xl font-bold mb-8 text-center">Shop by Category</h2>
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
          {categories.map((cat) => (
            <Link
              key={cat.slug}
              href={`/laptops?category=${cat.slug}`}
              className="flex flex-col items-center gap-3 p-6 rounded-xl border border-[var(--border)] bg-[var(--card)] hover:border-[var(--accent)] transition-colors"
            >
              <span className="text-3xl">{cat.emoji}</span>
              <span className="font-medium">{cat.name}</span>
            </Link>
          ))}
        </div>
      </div>

      {/* Features */}
      <div className="grid md:grid-cols-3 gap-8">
        <div className="p-6 rounded-xl border border-[var(--border)] bg-[var(--card)]">
          <h3 className="text-lg font-bold mb-2 text-[var(--accent)]">AI-Powered Chat</h3>
          <p className="text-[var(--muted)]">
            Tell our AI what you need and get personalized laptop recommendations with detailed explanations.
          </p>
        </div>
        <div className="p-6 rounded-xl border border-[var(--border)] bg-[var(--card)]">
          <h3 className="text-lg font-bold mb-2 text-[var(--accent)]">Side-by-Side Compare</h3>
          <p className="text-[var(--muted)]">
            Compare up to 4 laptops side by side with highlighted winners for every spec.
          </p>
        </div>
        <div className="p-6 rounded-xl border border-[var(--border)] bg-[var(--card)]">
          <h3 className="text-lg font-bold mb-2 text-[var(--accent)]">Real Reviews</h3>
          <p className="text-[var(--muted)]">
            Read reviews from real users across different use cases — programming, gaming, business, creative work.
          </p>
        </div>
      </div>
    </div>
  );
}
