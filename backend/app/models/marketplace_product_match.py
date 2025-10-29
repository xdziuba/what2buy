from pydantic import BaseModel, Field
from .product_info import ProductInfo

class MarketplaceProductMatch(BaseModel):
    marketplace: str = Field(..., description="The name of the marketplace (e.g., Amazon, eBay, etc.)")
    results: list[ProductInfo] = Field(..., description="A list of up to 3 products that best match the user's query on this marketplace. Each product must have a direct product URL, price, description, rating, and stock information.")