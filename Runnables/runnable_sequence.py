from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence

from dotenv import load_dotenv
import os

load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")  # your OpenRouter key
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"  # OpenRouter endpoint

model = ChatOpenAI()


prompt1 = PromptTemplate(
    template = "Write a joke about {topic}",
    input__variables = ["topic"]
)
prompt2 = PromptTemplate(
    template = "Explain the joke {topic}",
    input_variables = ["topic"]
)

parser = StrOutputParser()
chain = RunnableSequence( prompt1, model, parser, prompt2, model, parser)

result = chain.invoke({"topic": "AI"})
print(result)