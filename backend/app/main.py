import os
import asyncio
from dotenv import load_dotenv
import json
from typing import Optional, List

from fastapi import FastAPI

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_mcp_adapters.tools import load_mcp_tools

# TODO: Rozbić kod na osobne moduły
MARKETPLACES = ["Allegro", "Amazon", "eBay", "Kaufland", "Morele", "Neonet", "RTV Euro AGD", "X-Kom", "Mediaexpert"]

PROMPT_TEMPLATE = "You are an expert product research assistant. Your task is to help users find the best products based on their needs and preferences. To find products, first use the search_engine tool. When searching for products, use the web_data tool for the sales platform. If you don't find one, scrape the page as markdown. Use the web_data_bestbuy_products tool only to obtain information about a specific product you've already found in your search."

load_dotenv()
ai_model = ChatGoogleGenerativeAI(model=os.getenv("GENAI_MODEL"))

server_parameters = StdioServerParameters(
    command="npx",
    args=["@brightdata/mcp"],
    env= {
        "API_TOKEN": os.getenv("MCP_API_KEY"),
        "BROWSER_AUTH": os.getenv("MCP_SCRAPING_BROWSER_USER"),
        "WEB_UNLOCKER_ZONE": os.getenv("MCP_ULOCKER_ZONE")
    } # type: ignore
)

app = FastAPI(title="What2Buy", version="0.1", description="An AI-powered product research assistant.")


@app.get("/")
async def read_root():
    return {"Hello": "World"}