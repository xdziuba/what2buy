import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GENAI_API_KEY = os.getenv("GOOGLE_API_KEY")
    GENAI_MODEL = os.getenv("GENAI_MODEL")
    MCP_API_KEY = os.getenv("MCP_API_KEY")
    MCP_ULOCKER_ZONE = os.getenv("MCP_ULOCKER_ZONE")
    MCP_SCRAPING_BROWSER_USER = os.getenv("MCP_SCRAPING_BROWSER_USER")
    MARKETPLACES = ["Allegro", "Amazon", "eBay", "Kaufland", "Morele", "Neonet", "RTV Euro AGD", "X-Kom", "Mediaexpert"]
    PROMPT_TEMPLATE = "You are an expert product research assistant. Your task is to help users find the best products based on their needs and preferences. For each marketplace listed, you must: 1.Find up to 3 matching products that meet the user's requirements, 2.Prefer the most relevant and popular products, 3.Provide direct product page URLs (not search pages), 4. Include accurate price, description, rating, and stock information. If a marketplace has no suitable results, you may omit it or return an empty list for that marketplace. To find products, first use the search_engine tool. When searching for products, use the web_data tool for the sales platform. If you don't find one, scrape the page as markdown. Use the web_data_bestbuy_products tool only to obtain information about a specific product you've already found in your search."

config = Config()
