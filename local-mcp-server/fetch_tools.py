from fastmcp import Client
import asyncio

async def get_tools():
    # Connect to the MCP server via HTTP. The MCP Server is locally hosted. Status: Working.
    """This function retrieves all the tools exposed by the locally hosted MCP server. It calls the addition tool.
    All manual. In the next step, we will use an agent to call the tools."""

    async with Client("http://127.0.0.1:8082/mcp/") as client:
        tools = await client.list_tools()
        print("Tools exposed:", tools)

        result = await client.call_tool("add", {"a": 5, "b": 7})
        print("5 + 7 =", result)

if __name__ == "__main__":
  asyncio.run(get_tools())
