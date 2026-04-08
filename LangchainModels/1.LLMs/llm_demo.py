from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
#dotenv loads secret key in your current file/ load_dotenv i a function which loads env variable

load_dotenv()

llm = ChatGroq(
    model='llama-3.1-8b-instant',
)

result = llm.invoke('What is the capital of Turkey')
print(result.content)
