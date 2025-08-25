In this sub-repo, we create a small MCP server from our local machine and expose 4 tools via it for arithmetic operations.

- Once you run this file on your machine, you create a MCP Server.
- You can use it via cursor chat (in Agentic mode) or via simple Python.
- To use it via cursor chat, go to `Tools & Integrations` in cursor, `Add new MCP Server`, then add the `dict' below to your mcpServers json file
  ```
  "calculator": {
      "command": "python",
      "args": [
        "Path_to_the_file_where_MCP_Server_is_defined"       
      ]
    }
  ```
- Once this is done, you'd be able to use the tools of your local MCP Server, via cursor chat.
- For use via Python, you can connect to your local MCP Server using `FastMCP` or `mcp_use` libraries and use it.
