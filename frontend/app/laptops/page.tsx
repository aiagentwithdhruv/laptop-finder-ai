"use client";

import { Suspense, useEffect, useState, useCallback } from "react";
import { useSearchParams } from "next/navigation";
import { Laptop, PaginatedResponse } from "@/types/laptop";
import { apiFetch } from "@/lib/api";
import LaptopCard from "@/components/laptops/laptop-card";

export default function LaptopsPage() {
  return (
    <Suspense fallback={<div className="max-w-7xl mx-auto px-4 py-8">Loading...</div>}>
      <LaptopsContent />
    </Suspense>
  );
}

function LaptopsContent() {
  const searchParams = useSearchParams();
  const [data, setData] = useState<PaginatedResponse | null>(null);
  const [brands, setBrands] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState({
    brand: searchParams.get("brand") || "",
    category: searchParams.get("category") || "",
    min_price: "",
    max_price: "",
    sort_by: "price_asc",
    page: 1,
  });

  const fetchLaptops = useCallback(async () => {
    setLoading(true);
    const params = new URLSearchParams();
    if (filters.brand) params.set("brand", filters.brand);
    if (filters.category) params.set("category", filters.category);
    if (filters.min_price) params.set("min_price", filters.min_price);
    if (filters.max_price) params.set("max_price", filters.max_price);
    params.set("sort_by", filters.sort_by);
    params.set("page", String(filters.page));

    const result = await apiFetch<PaginatedResponse>(`/laptops?${params}`);
    setData(result);
    setLoading(false);
  }, [filters]);

  useEffect(() => {
    fetchLaptops();
  }, [fetchLaptops]);

  useEffect(() => {
    apiFetch<string[]>("/laptops/brands").then(setBrands);
  }, []);

  const categories = ["ultrabook", "gaming", "workstation", "business", "budget", "2in1"];

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">Browse Laptops</h1>

      <div className="flex gap-8">
        {/* Filters Sidebar */}
        <div className="w-64 shrink-0 space-y-6">
          <div>
            <h3 className="font-semibold mb-3 text-sm uppercase text-[var(--muted)]">Category</h3>
            <div className="space-y-2">
              <button
                onClick={() => setFilters({ ...filters, category: "", page: 1 })}
                className={`block text-sm ${!filters.category ? "text-[var(--accent)]" : "text-[var(--muted)] hover:text-white"}`}
              >
                All
              </button>
              {categories.map((cat) => (
                <button
                  key={cat}
                  onClick={() => setFilters({ ...filters, category: cat, page: 1 })}
                  className={`block text-sm capitalize ${filters.category === cat ? "text-[var(--accent)]" : "text-[var(--muted)] hover:text-white"}`}
                >
                  {cat}
                </button>
              ))}
            </div>
          </div>

          <div>
            <h3 className="font-semibold mb-3 text-sm uppercase text-[var(--muted)]">Brand</h3>
            <div className="space-y-2">
              <button
                onClick={() => setFilters({ ...filters, brand: "", page: 1 })}
                className={`block text-sm ${!filters.brand ? "text-[var(--accent)]" : "text-[var(--muted)] hover:text-white"}`}
              >
                All
              </button>
              {brands.map((brand) => (
                <button
                  key={brand}
                  onClick={() => setFilters({ ...filters, brand, page: 1 })}
                  className={`block text-sm ${filters.brand === brand ? "text-[var(--accent)]" : "text-[var(--muted)] hover:text-white"}`}
                >
                  {brand}
                </button>
              ))}
            </div>
          </div>

          <div>
            <h3 className="font-semibold mb-3 text-sm uppercase text-[var(--muted)]">Price Range</h3>
            <div className="flex gap-2">
              <input
                type="number"
                placeholder="Min"
                value={filters.min_price}
                onChange={(e) => setFilters({ ...filters, min_price: e.target.value, page: 1 })}
                className="w-full px-3 py-2 rounded bg-[var(--card)] border border-[var(--border)] text-sm"
              />
              <input
                type="number"
                placeholder="Max"
                value={filters.max_price}
                onChange={(e) => setFilters({ ...filters, max_price: e.target.value, page: 1 })}
                className="w-full px-3 py-2 rounded bg-[var(--card)] border border-[var(--border)] text-sm"
              />
            </div>
          </div>

          <div>
            <h3 className="font-semibold mb-3 text-sm uppercase text-[var(--muted)]">Sort By</h3>
            <select
              value={filters.sort_by}
              onChange={(e) => setFilters({ ...filters, sort_by: e.target.value, page: 1 })}
              className="w-full px-3 py-2 rounded bg-[var(--card)] border border-[var(--border)] text-sm"
            >
              <option value="price_asc">Price: Low to High</option>
              <option value="price_desc">Price: High to Low</option>
              <option value="rating">Top Rated</option>
              <option value="newest">Newest</option>
            </select>
          </div>
        </div>

        {/* Laptop Grid */}
        <div className="flex-1">
          {loading ? (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {Array.from({ length: 6 }).map((_, i) => (
                <div key={i} className="rounded-xl border border-[var(--border)] bg-[var(--card)] animate-pulse">
                  <div className="aspect-[4/3] bg-[#1a1a1a]" />
                  <div className="p-4 space-y-3">
                    <div className="h-3 bg-[#1a1a1a] rounded w-1/3" />
                    <div className="h-4 bg-[#1a1a1a] rounded w-2/3" />
                    <div className="h-6 bg-[#1a1a1a] rounded w-1/4" />
                  </div>
                </div>
              ))}
            </div>
          ) : data && data.items.length > 0 ? (
            <>
              <p className="text-sm text-[var(--muted)] mb-4">{data.total} laptops found</p>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {data.items.map((laptop) => (
                  <LaptopCard key={laptop.id} laptop={laptop} />
                ))}
              </div>
              {data.total_pages > 1 && (
                <div className="flex justify-center gap-2 mt-8">
                  {Array.from({ length: data.total_pages }).map((_, i) => (
                    <button
                      key={i}
                      onClick={() => setFilters({ ...filters, page: i + 1 })}
                      className={`w-10 h-10 rounded ${
                        data.page === i + 1
                          ? "bg-[var(--accent)] text-black"
                          : "bg-[var(--card)] border border-[var(--border)] hover:border-[var(--accent)]"
                      }`}
                    >
                      {i + 1}
                    </button>
                  ))}
                </div>
              )}
            </>
          ) : (
            <div className="text-center py-20 text-[var(--muted)]">
              <p className="text-lg">No laptops found</p>
              <p className="text-sm mt-2">Try adjusting your filters</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
