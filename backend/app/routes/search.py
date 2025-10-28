from fastapi import APIRouter, Query
from app.core.agent import Agent

agent_instance = Agent()
router = APIRouter(prefix="/search", tags=["search"])

@router.get("/")
async def search_for_products(query: str = Query(..., description="Phrase to search for")):
    # TODO: integrate with AI agent or marketplace service
    results = await agent_instance.run_search(query)
    return {"query": query, "results": results}  # Placeholder response