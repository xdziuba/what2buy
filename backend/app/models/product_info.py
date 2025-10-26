from pydantic import BaseModel, Field

class ProductInfo(BaseModel):
    name: str = Field(..., description="The name of the product")
    url: str = Field(..., description="The URL of the product page")
    price: float = Field(..., description="The price of the product in PLN")
    description: str = Field(..., description="A brief description of the product")
    rating: float = Field(..., description="The average user rating of the product (depends on the marketplace, for example stars, points, etc.)")
    in_stock: bool = Field(..., description="Availability of the product in stock")