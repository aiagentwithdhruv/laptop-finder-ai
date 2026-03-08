export interface LaptopSpec {
  cpu: string;
  cpu_brand: string;
  gpu: string;
  gpu_brand: string;
  ram_gb: number;
  ram_type: string;
  storage_gb: number;
  storage_type: string;
  display_size: number;
  display_resolution: string;
  display_type: string;
  display_refresh_rate: number;
  battery_wh: number;
  battery_life_hours: number;
  weight_kg: number;
  os: string;
  ports: string[];
  wifi: string;
  bluetooth: string;
  color: string;
  year: number;
}

export interface LaptopImage {
  id: string;
  url: string;
  alt_text: string;
  is_primary: boolean;
}

export interface Review {
  id: string;
  reviewer_name: string;
  rating: number;
  title: string;
  body: string;
  verified_purchase: boolean;
  helpful_count: number;
  use_case: string;
}

export interface Laptop {
  id: string;
  brand: string;
  model: string;
  slug: string;
  category: string;
  price: number;
  original_price: number | null;
  currency: string;
  description: string;
  highlights: string[];
  avg_rating: number;
  review_count: number;
  in_stock: boolean;
  primary_image: string | null;
  spec: LaptopSpec | null;
}

export interface LaptopDetail extends Laptop {
  images: LaptopImage[];
  reviews: Review[];
}

export interface PaginatedResponse {
  items: Laptop[];
  total: number;
  page: number;
  page_size: number;
  total_pages: number;
}
