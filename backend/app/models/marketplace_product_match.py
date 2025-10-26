from pydantic import BaseModel, Field
from .product_info import ProductInfo

class MarketplaceProductMatch(BaseModel):
    marketplace: str = Field(..., description="The name of the marketplace (e.g., Amazon, eBay, etc.)")
    results: list[ProductInfo] = Field(..., description="A list of matched products from the marketplace")