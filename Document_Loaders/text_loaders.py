from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")  # your OpenRouter key
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"  # OpenRouter endpoint

loader = TextLoader("THE-VERDICT.txt", encoding = "utf-8")
docs = loader.load()

model =  ChatOpenAI()
prompt = PromptTemplate(
    template = "Summarize the following text:\n {text}",
    input_variables = ["text"]
)
parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"text": docs[0].page_content})
print(result)
 # print(type(docs))
# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)
# print(type(docs[0]))