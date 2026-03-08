"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";
import { LaptopDetail } from "@/types/laptop";
import { apiFetch } from "@/lib/api";
import { formatPrice } from "@/lib/utils";

export default function LaptopDetailPage() {
  const { id } = useParams();
  const [laptop, setLaptop] = useState<LaptopDetail | null>(null);

  useEffect(() => {
    if (id) apiFetch<LaptopDetail>(`/laptops/${id}`).then(setLaptop);
  }, [id]);

  if (!laptop) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-8 animate-pulse">
        <div className="h-8 bg-[var(--card)] rounded w-1/3 mb-8" />
        <div className="grid md:grid-cols-2 gap-8">
          <div className="aspect-[4/3] bg-[var(--card)] rounded-xl" />
          <div className="space-y-4">
            <div className="h-6 bg-[var(--card)] rounded w-2/3" />
            <div className="h-10 bg-[var(--card)] rounded w-1/3" />
          </div>
        </div>
      </div>
    );
  }

  const spec = laptop.spec;

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <div className="grid md:grid-cols-2 gap-8 mb-12">
        {/* Images */}
        <div>
          <div className="aspect-[4/3] rounded-xl bg-[var(--card)] overflow-hidden mb-4">
            {laptop.images?.[0] ? (
              <img src={laptop.images[0].url} alt={laptop.images[0].alt_text} className="w-full h-full object-cover" />
            ) : (
              <div className="w-full h-full flex items-center justify-center text-6xl">💻</div>
            )}
          </div>
          {laptop.images?.length > 1 && (
            <div className="flex gap-2">
              {laptop.images.map((img) => (
                <div key={img.id} className="w-20 h-16 rounded border border-[var(--border)] overflow-hidden">
                  <img src={img.url} alt={img.alt_text} className="w-full h-full object-cover" />
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Info */}
        <div>
          <p className="text-sm text-[var(--accent)] font-medium uppercase mb-1">{laptop.brand}</p>
          <h1 className="text-3xl font-bold mb-4">{laptop.model}</h1>
          <div className="flex items-center gap-3 mb-4">
            <span className="text-yellow-400">{"★".repeat(Math.round(laptop.avg_rating))}</span>
            <span className="text-[var(--muted)]">{laptop.avg_rating}/5 ({laptop.review_count} reviews)</span>
          </div>
          <div className="flex items-center gap-3 mb-6">
            <span className="text-3xl font-bold">{formatPrice(laptop.price)}</span>
            {laptop.original_price && (
              <span className="text-lg text-[var(--muted)] line-through">{formatPrice(laptop.original_price)}</span>
            )}
          </div>
          <p className="text-[var(--muted)] mb-6">{laptop.description}</p>

          {laptop.highlights.length > 0 && (
            <div className="mb-6">
              <h3 className="font-semibold mb-2">Highlights</h3>
              <ul className="space-y-1">
                {laptop.highlights.map((h, i) => (
                  <li key={i} className="text-sm text-[var(--muted)]">✓ {h}</li>
                ))}
              </ul>
            </div>
          )}

          <div className="flex gap-3">
            <Link
              href={`/chat?about=${laptop.id}`}
              className="px-6 py-3 bg-[var(--accent)] text-black font-semibold rounded-lg hover:opacity-90"
            >
              Ask AI About This Laptop
            </Link>
            <Link
              href={`/compare?ids=${laptop.id}`}
              className="px-6 py-3 border border-[var(--border)] rounded-lg hover:border-[var(--accent)]"
            >
              Compare
            </Link>
          </div>
        </div>
      </div>

      {/* Specs */}
      {spec && (
        <div className="mb-12">
          <h2 className="text-2xl font-bold mb-6">Specifications</h2>
          <div className="grid md:grid-cols-2 gap-4">
            {[
              ["Processor", spec.cpu],
              ["Graphics", spec.gpu],
              ["RAM", `${spec.ram_gb}GB ${spec.ram_type}`],
              ["Storage", `${spec.storage_gb}GB ${spec.storage_type}`],
              ["Display", `${spec.display_size}" ${spec.display_type} ${spec.display_resolution} ${spec.display_refresh_rate}Hz`],
              ["Battery", `${spec.battery_life_hours}h (${spec.battery_wh}Wh)`],
              ["Weight", `${spec.weight_kg}kg`],
              ["OS", spec.os],
              ["WiFi", spec.wifi],
              ["Bluetooth", spec.bluetooth],
              ["Color", spec.color],
              ["Ports", spec.ports.join(", ")],
            ].map(([label, value]) => (
              <div key={label} className="flex justify-between py-3 border-b border-[var(--border)]">
                <span className="text-[var(--muted)]">{label}</span>
                <span className="font-medium text-right max-w-[60%]">{value}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Reviews */}
      {laptop.reviews?.length > 0 && (
        <div>
          <h2 className="text-2xl font-bold mb-6">Reviews ({laptop.review_count})</h2>
          <div className="space-y-4">
            {laptop.reviews.map((review) => (
              <div key={review.id} className="p-4 rounded-xl border border-[var(--border)] bg-[var(--card)]">
                <div className="flex items-center justify-between mb-2">
                  <div className="flex items-center gap-2">
                    <span className="text-yellow-400 text-sm">{"★".repeat(review.rating)}</span>
                    <span className="font-semibold text-sm">{review.title}</span>
                  </div>
                  <span className="text-xs px-2 py-1 rounded-full bg-[var(--accent-dim)] text-[var(--accent)]">
                    {review.use_case}
                  </span>
                </div>
                <p className="text-sm text-[var(--muted)] mb-2">{review.body}</p>
                <div className="flex items-center gap-3 text-xs text-[var(--muted)]">
                  <span>{review.reviewer_name}</span>
                  {review.verified_purchase && <span className="text-green-500">✓ Verified</span>}
                  <span>{review.helpful_count} found helpful</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
