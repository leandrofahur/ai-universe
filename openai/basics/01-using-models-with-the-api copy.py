# OpenAI
from openai import OpenAI

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

# print(type(client.models.list()))
# for model in client.models.list():
#     print(model)

# To create a API request:
response = client.responses.create(
    model="gpt-4o-mini",
    instructions="You are a gentle and polite Japanese language teacher. You are given a sentence in English and you need to translate it into Japanese.",
    input="How can I say: 'How are you?' in Japanese?",
    max_output_tokens=100,
    temperature=0.5
)

print(response.output_text)