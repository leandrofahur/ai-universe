# LangChain Tools:
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Initialize the LLM model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Define the list of message structure:
# Message structure: https://python.langchain.com/docs/concepts/messages/
# SystemMessage: https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html
# HumanMessage: https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html
message = [
    # This one is responsisble for "setting" the AI behaviour (input context)
    SystemMessage(
        content="You are an AI assistant ready to answer any question related to LLMs by the user."        
    ),
    HumanMessage(
        content="What are LLMs?"
    )
]

# Call the LLM model with the message structure
# AIMessage: https://python.langchain.com/docs/concepts/messages/#aimessage
# response = llm.invoke(message)

# print(type(response))
# print(response.content)

#  ------------------------------------------------------------------------------------------------------------------------------------
# PromptTemplate: https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html
system_prompt_template = "Translate the following English sentence {sentence} into {language} using {languague_type}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt_template),
        ("human", "{sentence}")
    ]
)
prompt = prompt_template.invoke({
    "sentence": "Please, have a seat.",
    "language": "Japanese",
    "languague_type": "hiragana"
})

# Print the prompt with the expected format, if everything is ok, just use the invoke method on it
# print(prompt)

response = llm.invoke(prompt)
print(response.content)

