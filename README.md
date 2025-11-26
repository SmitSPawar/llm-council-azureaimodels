# LLM Council (Azure OpenAI Edition)

!llmcouncil

## 🧠 What is LLM Council?
Instead of asking a single LLM (like GPT-4, GPT-4 Turbo, or GPT-4o), this project lets you create an **LLM Council** using **Azure OpenAI Service**. It’s a local web app that looks like ChatGPT but queries multiple Azure-hosted models, has them **review and rank each other’s responses**, and finally a **Chairman LLM** compiles the best final answer.

### 🔍 How It Works
1. **Stage 1: First Opinions**  
   Each Azure OpenAI model responds individually to your query. Responses are shown in a tab view for easy comparison.
2. **Stage 2: Review**  
   Each model anonymously reviews and ranks the others’ responses for accuracy and insight.
3. **Stage 3: Final Response**  
   The Chairman model synthesizes all responses into one final answer.