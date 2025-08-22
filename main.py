import asyncio
import os
from dotenv import load_dotenv
from fastmcp import FastMCP, Client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp_use import MCPClient, MCPAgent
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

load_dotenv()
import gradio as gr

async def create_mcp_server():
  """Spins a MCP client, defines a LLM object and creates an agent. Returns the MCP client and agent objects."""
    client = MCPClient.from_config_file(
        os.path.join(os.path.dirname(__file__), "airbnb_mcp.json")
    )    
  
  # llm = ChatGroq(
    #     groq_api_key = os.getenv("GROQ_API_KEY"),
    #     # model_name="llama3-8b-8192" #rate limit is 6k TPM
    #     model_name = "meta-llama/llama-4-maverick-17b-128e-instruct"
    # )
  
    llm = ChatOpenAI(
        model = "gpt-3.5-turbo",
        api_key=os.getenv("OPENAI_KEY"),
        temperature=0,
        max_retries=2,
    )

    agent = MCPAgent(llm=llm, client=client, max_steps=30)
    return [client, agent]

async def run_airbnb_mcp_server(query):
    """
      Function takes a user input (in human language form). 
      A MCP client is spun up, which connects to the Airbnb MCP Server.
      Agent selects the relevant tool among all the tools exposed by the MCP Server
    """
    client, agent = await create_mcp_server()
  
    system_prompt = "You are intelligent Chatbot to assist users in finding Airbnb listings. Current year is 2025. If user shares his total budget, use it as maxPrice, but if user asks his max cost per night, multiply it with total number of stay days to find maxPrice" \

    sample_query = "I need a place to stay in Bhubaneswar for me on 30th August this year. Show me top 5 options with prices and ratings. I need a 2 bedroom apartment with a kitchen and wifi..Max price is 10,000. Also, I need to know the cancellation policy. Please provide me with the details of the top 5 options available."

    try:
        result = await agent.run(
            system_prompt + query
        )
        print("Agent Result:", result)
        
    finally:
        if client.sessions:
            await client.close_all_sessions()

    return result

def interface():
    with gr.Blocks() as demo:
        gr.Markdown("# MCP Demo")
        name = gr.Textbox(label="Query about Airbnb", placeholder="")
        query = gr.Button("Search")
        output = gr.Markdown(label="Airbnb Response")
          
        query.click(run_airbnb_mcp_server, inputs=name, outputs=output)

    return demo

if __name__ == "__main__":
    interface().launch(share=True)

