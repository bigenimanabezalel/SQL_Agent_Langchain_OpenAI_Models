from os import environ
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import SQLDatabaseToolkit

# Custom modules
import load_env_vars
from postgres_connection import db_object

# API Key
api_key = environ.get('OPENAI_API_KEY', '')

# Model
model = ChatOpenAI(model='gpt-4o', api_key=api_key)

# Object
toolkit = SQLDatabaseToolkit(db=db_object, llm=model)

# .get_tools()
tools = toolkit.get_tools()

# View the different tools
for tool in tools:
    print(f"{tool.name}: {tool.description}\n")
