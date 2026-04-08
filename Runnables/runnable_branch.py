from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableLambda, RunnableBranch

from dotenv import load_dotenv
import os

load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")  # your OpenRouter key
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"  # OpenRouter endpoint

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template = "Write a report on {topic}",
    input_variables = ["topic"]
)
prompt2 = PromptTemplate(
    template = "Summarize the report {topic}",
    input_variables = ["topic"]
)
parser = StrOutputParser()

joke_gen_chain = RunnableSequence( prompt1, model, parser)

parallel_chain = RunnableBranch(
    (lambda x : len(x.split()) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)
result = final_chain.invoke({"topic" : "Isreal bombing innocent civillians be it kids"})
print(result)