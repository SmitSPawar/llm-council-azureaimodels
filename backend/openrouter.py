
"""Azure OpenAI client for making LLM requests (replaces OpenRouter)."""

from openai import OpenAI
from typing import List, Dict, Any, Optional
import asyncio
from backend.config import AZURE_API_KEY, AZURE_ENDPOINT  # Ensure these exist

# Initialize Azure OpenAI client (same as your working code)
client = OpenAI(
    base_url=f"{AZURE_ENDPOINT}/openai/v1",  # Matches your working snippet
    api_key=AZURE_API_KEY
)

async def query_model(
    model: str,  # Azure deployment name
    messages: List[Dict[str, str]],
    timeout: float = 120.0
) -> Optional[Dict[str, Any]]:
    """
    Query a single Azure OpenAI deployment using Chat Completions API.
    """
    try:
        completion = client.chat.completions.create(
            model=model,  # Deployment name (e.g., council-Phi-4-mini-reasoning)
            messages=messages
        )

        message = completion.choices[0].message
        return {
            "content": message.content,
            "reasoning_details": getattr(message, "reasoning_details", None)
        }

    except Exception as e:
        print(f"Error querying model {model}: {e}")
        return None

async def query_models_parallel(
    models: List[str],
    messages: List[Dict[str, str]]
) -> Dict[str, Optional[Dict[str, Any]]]:
    """
    Query multiple Azure OpenAI deployments in parallel.
    """
    tasks = [query_model(model, messages) for model in models]
    responses = await asyncio.gather(*tasks)
    return {model: response for model, response in zip(models, responses)}
