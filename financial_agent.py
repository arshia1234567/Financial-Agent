from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os

load_dotenv()

# Now you can access the environment variables
groq_api_key = os.getenv('GROQ_API_KEY')
#web search agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
model=Groq(id="llama3-70b-8192"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)
#financial agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-70b-8192"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True),

    ],
    instructions=["use tables to display the data "],
    show_tool_calls=True,
    markdown=True,
    
)
multi_ai_agent=Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama3-70b-8192"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDIA", stream=True)


