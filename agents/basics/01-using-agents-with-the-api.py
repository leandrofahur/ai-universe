# OpenAI
from openai import OpenAI

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()
print(client)