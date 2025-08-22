# What it does

- Spins up a MCP client and connects to Airbnb MCP server.
- Uses the tools made available by MCP server to respond to user queries regarding Airbnb rooms.

# Techstack
- `mcp-use` for MCP
- `langchain-openai` for LLMs
- `gradio` for interface

# How to use it
- Clone the repo
- Ensure you have `Node.js` on your system
- Make an `.env` file at the root of the repo and put your OPENAI API KEY against `OPENAI_KEY`
- Install the libraries in `requirements.txt`
- Execute `python main.py`

# Precaution
- Ensure your API KEY can handle atleast 6k tokens per minute. Paid API keys work the best to avoid rate limits.
