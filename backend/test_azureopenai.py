
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Read from environment
AZURE_OPENAI_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_ENDPOINT")  # e.g., https://nouryonazai.openai.azure.com
AZURE_OPENAI_DEPLOYMENT = "council-Phi-4-mini-reasoning"
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_API_VERSION", "2024-06-01")

# Validate environment variables
if not AZURE_OPENAI_API_KEY or not AZURE_OPENAI_ENDPOINT:
    raise RuntimeError("Missing Azure OpenAI configuration. Check .env file.")

# Build base URL (Azure-specific)
base_url = f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{AZURE_OPENAI_DEPLOYMENT}?api-version={AZURE_OPENAI_API_VERSION}"

# Initialize client
client = OpenAI(api_key=AZURE_OPENAI_API_KEY, base_url=base_url)

# Make a simple request using Chat Completions API
try:
    completion = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,  # Deployment name
        messages=[
            {"role": "user", "content": "What is the capital of France?"}
        ],
        temperature=0,
        max_tokens=50
    )

    print("Answer:", completion.choices[0].message.content)

except Exception as e:
    print(f"Azure OpenAI request failed: {e}")
