from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=OpenAIChat(id='gpt-4.1-mini'),
    tools=[TavilyTools()],
    debug_mode=True
)

agent.print_response('Use your tools to search for potential financial investment opportunities today')