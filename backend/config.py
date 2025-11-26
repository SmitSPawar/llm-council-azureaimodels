"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()


# Azure credentials from .env
AZURE_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION", "2024-02-15-preview")


# OpenRouter API key
#OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

#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
# Council members - list of OpenRouter model identifiers


#COUNCIL_MODELS = [
#    "openai/gpt-oss-20b:free",
#    "qwen/qwen3-coder:free",
#    "z-ai/glm-4.5-air:free",
#    "x-ai/grok-4.1-fast:free",
#]
COUNCIL_MODELS = [
    "grok-3",
    "gpt-4o",
    "gpt-4o-mini",
    "gpt-5.1-codex"
]


# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "gpt-5.1-codex"

# OpenRouter API endpoint
#OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
