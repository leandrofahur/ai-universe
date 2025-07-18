from openai import OpenAI
import requests, json
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

from openai import OpenAI

client = OpenAI()

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']


tools = [{
    "type": "function",
    "name": "get_weather",
    "description": "Get current temperature for provided coordinates in celsius.",
    "parameters": {
        "type": "object",
        "properties": {
            "latitude": {"type": "number"},
            "longitude": {"type": "number"}
        },
        "required": ["latitude", "longitude"],
        "additionalProperties": False
    },
    "strict": True
}]

input_messages = [{"role": "user", "content": "What's the weather like in Paris today?"}]

response = client.responses.create(
    model="gpt-4.1",
    input=input_messages,
    tools=tools
)

print(response.output)

tool_call = response.output[0]
args = json.loads(tool_call.arguments)

print(args["latitude"], args["longitude"])
print(get_weather(args["latitude"], args["longitude"]))