from pydantic import BaseModel, Field
from .marketplace_product_match import MarketplaceProductMatch

class SearchResult(BaseModel):
    marketplaces: list[MarketplaceProductMatch] = Field(..., description="A list of all results grouped by marketplace")