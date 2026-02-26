# LangGraph

AI agent workflows built with [LangGraph](https://langchain-ai.github.io/langgraph/), [LangChain](https://www.langchain.com/) and OpenAI.

## Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager

## Setup

```bash
uv venv
uv sync
```

Create a `.env` file in the project root with your API keys:

```
OPENAI_API_KEY=your-key-here
```

## Usage

```bash
uv run python main.py
```

## Development

```bash
uv add ipykernel --dev
uv run langgraph dev
```

## Project Structure

```
├── .gitignore
├── .python-version
├── df.ipynb            # Experimentation notebook
├── main.py             # Entry point
├── pyproject.toml      # Dependencies and project config
├── README.md
└── uv.lock
```
