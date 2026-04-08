from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")  # your OpenRouter key
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"  # OpenRouter endpoint

prompt1 = PromptTemplate(
    template = "Give a detailed report on the {topic}",
    input_variables = ["topic"]
)

prompt2  = PromptTemplate(
    template = "Summarize the following report {report} in 5 sentencs",
    input_variables = ["report"]
)
parser = StrOutputParser()

model = ChatOpenAI()

chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({"topic": "Space exploration"})
print(result)
chain.get_graph().print_ascii()