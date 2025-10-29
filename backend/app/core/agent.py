from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_mcp_adapters.tools import load_mcp_tools

from .config import config
from app.models.search_result import SearchResult

class Agent:
    def __init__(self) -> None:
        self.model = ChatGoogleGenerativeAI(model=config.GENAI_MODEL)
        self.server_parameters = StdioServerParameters(
            command="npx",
            args=["@brightdata/mcp"],

            env= {
                "API_TOKEN": config.MCP_API_KEY,
                "BROWSER_AUTH": config.MCP_SCRAPING_BROWSER_USER,
                "WEB_UNLOCKER_ZONE": config.MCP_ULOCKER_ZONE
            } # type: ignore
        )

    async def run_search(self, user_query: str):
        async with stdio_client(self.server_parameters) as (r, w):
            async with ClientSession(r, w) as session:
                await session.initialize()

                agent = create_agent(self.model, await load_mcp_tools(session=session), response_format=SearchResult)
                full_query = f"{user_query}\nMarketplaces: {','.join(config.MARKETPLACES)}"

                response = await agent.ainvoke(
                    {
                        'messages': [
                            {"role": "system", "content": config.PROMPT_TEMPLATE},
                            {"role": "user", "content": full_query}
                        ]
                    }
                )
                return response['structured_response']