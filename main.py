from importlib.metadata import version
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

core_version = version("langchain_core")
graph_version = version("langgraph")

print(f"langchain_core version: {core_version}")
print(f"langgraph version: {graph_version}")


def main():
    # Testing OPEN AI LLM
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    response = llm.invoke("Write a short poem about the LangChain library.")
    print(f"Response from ChatOpenAI: {response}")

    # Testing ANTHROPIC LLM
    llm = ChatAnthropic(model="claude-sonnet-4-6", temperature=0)
    response = llm.invoke("Write a short poem about the LangChain library.")
    print(f"Response from ChatAnthropic: {response}")

    print("Setup Complete!")


if __name__ == "__main__":
    main()
