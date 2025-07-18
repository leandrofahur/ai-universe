import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

def main():
    client = OpenAI()
    print(client)

if __name__ == "__main__":
    main()

