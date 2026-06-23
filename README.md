# GenAI Project Boilerplate

A boilerplate project for building generative AI applications using LangChain, LLMs, and agent frameworks.

## Overview

This project provides a foundation for developing GenAI solutions with support for:
- Multiple LLM providers (OpenAI, Anthropic)
- LangChain ecosystem for prompt management and chains
- LanGraph for building agentic workflows
- Environment configuration management

## Dependencies

```bash
uv add langchain langchain_core langchain-openai langgraph langchain-anthropic python-dotenv
```

### Key Packages
- **langchain** - LLM orchestration framework
- **langchain_core** - Core abstractions and types
- **langchain-openai** - OpenAI integration
- **langgraph** - Graph-based agent framework
- **langchain-anthropic** - Anthropic models integration
- **python-dotenv** - Environment variable management

## Project Structure

```
GenAIProjectBoilerplateCode/
└── README.md
└── .env    (this will be created when we first run the main.py)
└── main.py (contains sample code.)
└── .gitignore
└── pyproject.toml  (most important file it contains all dependices)

```

## Getting Started
Prerequisites - uv should be installed on you machine before working on this.

1. Install dependencies using `uv`
