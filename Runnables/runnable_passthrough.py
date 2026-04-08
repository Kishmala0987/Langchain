from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough

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

joke_gen_ai = RunnableSequence( prompt1, model, parser)
parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen_ai, parallel_chain)
result = final_chain.invoke({"topic": "war"})
print(result)
final_chain.get_graph().print_ascii()