from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")  # your OpenRouter key
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"  # OpenRouter endpoint


embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = [
    "The capital of Pakistan is Islamabad.",
    "The capital of France is Paris.",
    "The capital of Japan is Tokyo."
]

result = embeddings.embed_documents(documents)
print(len(result))

print(str(result))