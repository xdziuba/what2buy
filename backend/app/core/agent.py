from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_openai import ChatOpenAI # type: ignore
from langchain.agents import create_agent
from langchain_mcp_adapters.tools import load_mcp_tools

from .config import config
from app.models.search_result import SearchResult

class Agent:
    def __init__(self) -> None:
        self.model = ChatOpenAI(model='gpt-4o')
        self.server_parameters = StdioServerParameters(
            command="npx",
            args=["@brightdata/mcp"],

            env= {
                "API_TOKEN": config.MCP_API_KEY,
                "BROWSER_AUTH": config.MCP_SCRAPING_BROWSER_USER,
                "WEB_UNLOCKER_ZONE": config.MCP_ULOCKER_ZONE
            } # type: ignore
        )


    async def run_search(self, user_query: str, selected_marketplaces: list[str]):
        async with stdio_client(self.server_parameters) as (r, w):
            async with ClientSession(r, w) as session:
                await session.initialize()

                tools = await load_mcp_tools(session=session)
                allowed = {"search_engine", "web_data"}
                tools = [t for t in tools if t.name in allowed]
                agent = create_agent(self.model, tools=tools, response_format=SearchResult)
                full_query = f"{user_query}\nMarketplaces: {','.join(selected_marketplaces)}"

                response = await agent.ainvoke(
                    {
                        'messages': [
                            {"role": "system", "content": config.PROMPT_TEMPLATE},
                            {"role": "user", "content": full_query}
                        ]
                    }
                )

                try:
                    return [response['structured_response']]
                except Exception as e:
                    return [f'Error: Unable to parse response. ({e})']