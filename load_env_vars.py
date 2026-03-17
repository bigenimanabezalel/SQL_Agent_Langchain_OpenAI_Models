from os import getcwd
from dotenv import load_dotenv

# Environment path
env_path = getcwd() + r"\.venv\pyvenv.cfg"

# Load environment variables
load_dotenv(env_path)





