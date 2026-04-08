from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")  # your OpenRouter key
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting style.",
    "Sachin Tendulkar is a former Indian cricketer known for his record-breaking performances.",
    "Babar Azam is a Pakistani cricketer known for his elegant stroke play."
    "Steve Smith is an Australian cricketer known for his unorthodox batting technique."
]

query = "Tell me about world's best batsman."
doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
most_similar_doc_index = np.argmax(similarities)
most_similar_doc = documents[most_similar_doc_index]
print("Query:", query)
print("Most similar document:", most_similar_doc)
print("Similarity score:", similarities[most_similar_doc_index])