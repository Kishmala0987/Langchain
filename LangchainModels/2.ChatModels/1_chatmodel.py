from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
#dotenv loads secret key in your current file/ load_dotenv i a function which loads env variable

load_dotenv()

llm = ChatGroq(
    model='llama-3.1-8b-instant',
    temperature = 0.1
)

result = llm.invoke('Write a 5 line poem on Ottomon Empire')
print(result.content)
