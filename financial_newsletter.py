import os
import requests
from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from sendgrid.helpers.mail import Mail, Email, To, Content
import litellm
from agno.models.litellm import LiteLLM

load_dotenv()
litellm.drop_params = True

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

    # Convert mail object to JSON
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
    system_message='You are a senior financial specialist and market researcher.',
    model=LiteLLM(
        id="gpt-5-mini",
        name="LiteLLM",
        api_base=os.getenv('LITELLM_BASE_URL'),
        temperature=0.7
    ),
    tools=[
        TavilyTools(
            search_depth="basic",
            max_tokens=150
        ),
        send_email_sendgrid_api_tool
    ],
    markdown=True
)

if __name__ == '__main__':
    from prompt import instructions
    agent.run(instructions)