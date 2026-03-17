from os import environ
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

# Custom modules
import load_env_vars
from agent_toolkit import tools

# Model
api_key = environ.get('OPENAI_API_KEY')
model = ChatOpenAI(model='gpt-4o', api_key=api_key)

# Object
agent = create_agent(
    model=model,
    tools=tools
)

# Question
question = "Which customers are in common between regions?"

# Get the response
for step in agent.stream(
    {"messages": [{"role": "user", "content": question}]},
    stream_mode="values"
):
    # For each step, you want to get the last message and pretty print it
    step['messages'][-1].pretty_print()


