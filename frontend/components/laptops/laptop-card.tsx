"use client";

import Link from "next/link";
import { Laptop } from "@/types/laptop";
import { formatPrice } from "@/lib/utils";

export default function LaptopCard({ laptop }: { laptop: Laptop }) {
  return (
    <Link
      href={`/laptops/${laptop.id}`}
      className="group block rounded-xl border border-[var(--border)] bg-[var(--card)] overflow-hidden hover:border-[var(--accent)] transition-colors"
    >
      <div className="aspect-[4/3] bg-[#1a1a1a] flex items-center justify-center overflow-hidden">
        {laptop.primary_image ? (
          <img
            src={laptop.primary_image}
            alt={`${laptop.brand} ${laptop.model}`}
            className="w-full h-full object-cover group-hover:scale-105 transition-transform"
          />
        ) : (
          <div className="text-4xl">💻</div>
        )}
      </div>
      <div className="p-4">
        <p className="text-xs text-[var(--accent)] font-medium uppercase mb-1">{laptop.brand}</p>
        <h3 className="font-semibold text-sm mb-2 line-clamp-2">{laptop.model}</h3>
        <div className="flex items-center gap-2 mb-3">
          <span className="text-yellow-400 text-sm">{"★".repeat(Math.round(laptop.avg_rating))}</span>
          <span className="text-xs text-[var(--muted)]">({laptop.review_count})</span>
        </div>
        {laptop.spec && (
          <div className="flex flex-wrap gap-1.5 mb-3">
            <span className="text-xs px-2 py-0.5 rounded-full bg-[var(--accent-dim)] text-[var(--accent)]">
              {laptop.spec.ram_gb}GB RAM
            </span>
            <span className="text-xs px-2 py-0.5 rounded-full bg-[var(--accent-dim)] text-[var(--accent)]">
              {laptop.spec.storage_gb}GB
            </span>
            <span className="text-xs px-2 py-0.5 rounded-full bg-[var(--accent-dim)] text-[var(--accent)]">
              {laptop.spec.cpu_brand}
            </span>
          </div>
        )}
        <div className="flex items-center gap-2">
          <span className="text-lg font-bold">{formatPrice(laptop.price)}</span>
          {laptop.original_price && (
            <span className="text-sm text-[var(--muted)] line-through">
              {formatPrice(laptop.original_price)}
            </span>
          )}
        </div>
      </div>
    </Link>
  );
}
