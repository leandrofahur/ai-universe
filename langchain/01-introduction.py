# Third-party modules:
from langchain_openai import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

from dotenv import load_dotenv

# Configuration variables:
load_dotenv()
openai_model = "gpt-4o-mini"

# Initialize the LLMs we will require:
logical_llm = ChatOpenAI(temperature=0.1, model=openai_model)
creative_llm = ChatOpenAI(temperature=0.9, model=openai_model)

# TASK: LangChain will aid to generate an article following the requirements below:
# 1. Title
# 2. Hook
# 3. Purpose
# 4. Overview
# 5. Sections
# 6. Conclusion
# 7. A thumbnail / hero image for our article.

article_prompt = f"""
    🎯 Title: Exploring LangChain: The Core Concepts You Need to Know

    🔥 Hook: Are you curious about the power of language models but unsure where to start? LangChain is here to help you harness the potential of AI-driven natural language processing. Let's dive into its core concepts and see how it can revolutionize your projects!

    🎯 Purpose: This article aims to introduce the essential concepts behind LangChain, a framework for building applications powered by large language models. We'll explore what LangChain is, its key features, and how you can leverage it in your own projects.

    🧭 Overview: By the end of this post, you'll have a solid understanding of LangChain, including:

    What LangChain is and why it matters
    The core components that make up the framework
    How to integrate LangChain into your applications
    Some real-world use cases and examples
    
    📚 Sections: Let's break down these concepts one by one.

    What is LangChain? LangChain is an open-source framework that allows developers to easily build applications powered by large language models (LLMs) like GPT-3, Llama, and others. It provides a set of tools and abstractions for handling the complexities of working with LLMs, making it simpler to integrate AI into your projects.

    Key Components LangChain has several core components that work together to enable powerful language model applications:

    Chains: Reusable sequences of calls between components, allowing you to define complex workflows.
    Prompts: The natural language inputs given to the LLM to generate responses.
    Agents: Intelligent actors that can take actions based on their understanding of a prompt or chain.
    Memory: A way to store and retrieve information for use in chains, enabling context-aware interactions.
    Storage: Interfaces for reading from and writing to external data sources like databases or APIs.
    Vector Stores: Tools for storing, indexing, and retrieving semantic embeddings of text data.
    Integrating LangChain To use LangChain in your project, you'll typically follow these steps:

    Define a chain that specifies the sequence of operations needed to achieve your goal.

    Create prompts tailored to guide the LLM towards the desired output.

    Optionally, define an agent to take actions based on the prompt or chain.

    Set up memory and storage components as needed for accessing external data.

    Initialize a LangChain instance with your configured components.

    Call the chain's run method to execute the sequence and get the result.

    Use Cases LangChain has a wide range of potential applications, from chatbots and virtual assistants to automated content generation and data analysis. Some examples include:
    Building a chatbot for customer support that can answer questions based on a knowledge base.
    Generating summaries or insights from large text documents using an LLM's language understanding capabilities.
    Creating interactive fiction or roleplaying game scenarios driven by natural language input.
    Automatically generating code snippets, documentation, or entire programs based on natural language descriptions.
    
    🎁 Conclusion: LangChain is a powerful tool for harnessing the potential of large language models in your applications. By understanding its core concepts and components, you can start building AI-driven solutions that leverage the immense capabilities of LLMs. Whether you're looking to create chatbots, generate content, or analyze data, LangChain provides the foundation you need. So why wait? Start exploring the possibilities today!    
    
    🖼️ Thumbnail: A thumbnail / hero image for our article.
"""


system_prompt = SystemMessagePromptTemplate.from_template(f"""You are a helpful AI assistant that generates full article based on the user's outlined.""")
human_prompt = HumanMessagePromptTemplate.from_template("""Generate an article based on my outline: {article_outline}""", input_variables=["article_outline"])
chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

logical_chain = chat_prompt | logical_llm
creative_chain = chat_prompt | creative_llm

logical_chain_output = logical_chain.invoke({"article_outline": article_prompt})
creative_chain_output = creative_chain.invoke({"article_outline": article_prompt})

print(logical_chain_output.content)
print("\n\n")
print("-" * 100)
print("\n\n")
print(creative_chain_output.content)





