"use client";

import { useState, useEffect } from "react";
import { Laptop } from "@/types/laptop";
import { apiFetch } from "@/lib/api";
import { formatPrice } from "@/lib/utils";

interface SpecComparison {
  field: string;
  label: string;
  values: Record<string, string>;
  winner: string | null;
}

interface ComparisonResult {
  laptops: Array<{ id: string; brand: string; model: string; price: number; avg_rating: number; primary_image: string | null }>;
  specs: SpecComparison[];
  summary: string;
}

export default function ComparePage() {
  const [allLaptops, setAllLaptops] = useState<Laptop[]>([]);
  const [selectedIds, setSelectedIds] = useState<string[]>([]);
  const [comparison, setComparison] = useState<ComparisonResult | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    apiFetch<{ items: Laptop[] }>("/laptops?page_size=50").then((r) => setAllLaptops(r.items));
  }, []);

  async function handleCompare() {
    if (selectedIds.length < 2) return;
    setLoading(true);
    const result = await apiFetch<ComparisonResult>("/compare", {
      method: "POST",
      body: JSON.stringify({ laptop_ids: selectedIds }),
    });
    setComparison(result);
    setLoading(false);
  }

  function toggleLaptop(id: string) {
    setSelectedIds((prev) =>
      prev.includes(id) ? prev.filter((x) => x !== id) : prev.length < 4 ? [...prev, id] : prev
    );
    setComparison(null);
  }

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-2">Compare Laptops</h1>
      <p className="text-[var(--muted)] mb-8">Select 2-4 laptops to compare side by side</p>

      {/* Selector */}
      <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-3 mb-8">
        {allLaptops.map((l) => (
          <button
            key={l.id}
            onClick={() => toggleLaptop(l.id)}
            className={`p-3 rounded-lg border text-left text-xs transition-colors ${
              selectedIds.includes(l.id)
                ? "border-[var(--accent)] bg-[var(--accent-dim)]"
                : "border-[var(--border)] bg-[var(--card)] hover:border-[var(--accent)]"
            }`}
          >
            <p className="font-medium truncate">{l.brand} {l.model}</p>
            <p className="text-[var(--muted)]">{formatPrice(l.price)}</p>
          </button>
        ))}
      </div>

      {selectedIds.length >= 2 && (
        <button
          onClick={handleCompare}
          disabled={loading}
          className="mb-8 px-8 py-3 bg-[var(--accent)] text-black font-semibold rounded-lg hover:opacity-90 disabled:opacity-50"
        >
          {loading ? "Comparing..." : `Compare ${selectedIds.length} Laptops`}
        </button>
      )}

      {/* Comparison Table */}
      {comparison && (
        <div className="overflow-x-auto">
          <p className="text-sm text-[var(--muted)] mb-6 p-4 rounded-lg bg-[var(--card)] border border-[var(--border)]">
            {comparison.summary}
          </p>

          <table className="w-full border-collapse">
            <thead>
              <tr>
                <th className="text-left p-3 border-b border-[var(--border)] text-sm text-[var(--muted)]">Spec</th>
                {comparison.laptops.map((l) => (
                  <th key={l.id} className="p-3 border-b border-[var(--border)] text-center">
                    <p className="font-semibold text-sm">{l.brand}</p>
                    <p className="text-xs text-[var(--muted)]">{l.model}</p>
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {comparison.specs.map((spec) => (
                <tr key={spec.field}>
                  <td className="p-3 border-b border-[var(--border)] text-sm text-[var(--muted)]">{spec.label}</td>
                  {comparison.laptops.map((l) => {
                    const name = `${l.brand} ${l.model}`;
                    const isWinner = spec.winner === name;
                    return (
                      <td
                        key={l.id}
                        className={`p-3 border-b border-[var(--border)] text-center text-sm ${
                          isWinner ? "text-green-400 font-semibold" : ""
                        }`}
                      >
                        {spec.values[name] || "N/A"}
                        {isWinner && " ✓"}
                      </td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
