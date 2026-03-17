from os import environ
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine

# # Custom imports
# import load_env_vars


from dotenv import load_dotenv
import os
from pathlib import Path

# Path to your .env
env_path = Path(__file__).parent / ".venv\\pyvenv.cfg"

# Load it
load_dotenv(dotenv_path=env_path)

# Connection String
host = environ.get('POSTGRES_HOST')
user = environ.get('POSTGRES_USER')
password = environ.get('POSTGRES_PASSWORD')
port = environ.get('POSTGRES_PORT')
database = environ.get('POSTGRES_DATABASE')



print(host, port)

connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'


# Build the engine
engine = create_engine(connection_string)

# Build the database object
db_object = SQLDatabase(engine=engine)




