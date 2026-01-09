from pydantic import BaseModel, Field
from typing import List
from .product_specification import Specification

class ProductInfo(BaseModel):
    name: str = Field(..., description="The name of the product")
    url: str = Field(..., description="The direct URL of the exact product page where the product details (price, rating, description) were taken from. Never return a search or category URL. Always point to a specific product detail page.")
    price: float = Field(..., description="The price of the product in PLN")
    #description: str = Field(..., description="A brief description of the product")
    rating: float = Field(..., description="The average user rating of the product (depends on the marketplace, for example stars, points, etc.)")
    in_stock: bool = Field(..., description="Availability of the product in stock")
    specifications: List[Specification] = Field(..., description="A list of at least 6 key specifications of the product, where each specification is a name-value pair. Ensure consistency in specification keys across different products. For example, if 'Battery Life' is a key for one product, it should also be a key for other products when applicable.")