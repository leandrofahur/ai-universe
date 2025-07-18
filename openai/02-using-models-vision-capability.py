# OpenAI
from openai import OpenAI

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

import base64

client = OpenAI()

prompt = """
A realistic image of a black cat trying to steal it's owner's deep fried chicken from the table.
"""

result = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    style="vivid",
    n=1
)

print(result)