export interface Specification {
  name: string
  value: string
}

export interface ProductInfo {
  name: string
  url: string
  price: number
  rating: number
  in_stock: boolean
  specifications: Specification[]
}

export interface MarketplaceProductMatch {
  marketplace: string
  results: ProductInfo[]
}

export interface SearchResult {
  marketplaces: MarketplaceProductMatch[]
}
