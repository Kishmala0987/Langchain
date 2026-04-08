from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")  # your OpenRouter key
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"  # OpenRouter endpoint


embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

result = embeddings.embed_query("What is the capital of Pakistan?")
print(result)