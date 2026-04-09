import os
import requests
from sendgrid.helpers.mail import Mail, Email, To, Content
from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.huggingface import HuggingFace

load_dotenv()

def send_email_sendgrid_api_tool(subject, content):
    """Send email via SendGrid Web API"""

    # Build mail object
    message = Mail()
    message.from_email = Email(os.getenv('EMAIL_ADDRESS'))
    message.subject = subject
    message.add_content(Content('text/html', content))

    recipients = os.getenv('RECIPIENTS').split(',')

    for recipient in recipients:
        message.add_to(To(recipient))

    # Convert Mail object to JSON
    payload = message.get()
    
    # Set up new request
    headers = {
        'Authorization': f'Bearer {os.getenv('SENDGRID_API_KEY')}',
        'Content-Type': 'application/json'
    }
    
    proxies = {
        'https': os.getenv('HTTPS_PROXY')
    }

    try:
        response = requests.post(
            'https://api.sendgrid.com/v3/mail/send',
            headers=headers,
            json=payload,
            proxies=proxies,
            timeout=30
        )

        return str(response.status_code) + ' - Email successufully sent!'
        
    except Exception as e:
        return f'Exception: {e}'

# Set up Agno agent
agent = Agent(
    model=HuggingFace(
        id='openai/gpt-oss-120b',
    ),
    tools=[TavilyTools(),send_email_sendgrid_api_tool],
    debug_mode=False
)

if __name__ == '__main__':
    from prompt import agent_prompt
    agent.run(agent_prompt)