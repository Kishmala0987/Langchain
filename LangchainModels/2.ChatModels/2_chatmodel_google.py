from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
#dotenv loads secret key in your current file/ load_dotenv i a function which loads env variable

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)

result = llm.invoke('Write a 5 line poem on Ottomon Empire')
print(result.content)
