from fastapi import APIRouter, Query
from app.core.agent import Agent

agent_instance = Agent()
router = APIRouter(prefix="/search", tags=["search"])

@router.get("/")
async def search_for_products(query: str = Query(..., description="Phrase to search for"), marketplaces: list[str] = Query([], description="List of marketplaces to search in")):
    results = await agent_instance.run_search(query, marketplaces)
    return {"query": query, "results": results}