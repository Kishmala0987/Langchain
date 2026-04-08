from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv
import os

load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")  # your OpenRouter key
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"  # OpenRouter endpoint

parser = StrOutputParser()
model = ChatOpenAI()



class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object = Feedback)
prompt1 = PromptTemplate(
    template = "Classify the sentiment of the following feedback text into positive or negative:\n{feedback} \n{format_instructions}",
    input_variables = ["feedback"],
    partial_variables = {"format_instructions": parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template = "Write an appropriate response to this positive feedback: {feedback}",
    input_variables = ["feedback"]
)

prompt3 = PromptTemplate(
    template = "Write an appropriate response to this negative feedback: {feedback}",
    input_variables = ["feedback"]
)

# Runnable branch main tupks bhejto ho, har tuple main 2 chezen bhejty hain pehle condition or us condition k true hone pr kons chain exectue krna chaty, or agar koi bhi chain execute nahi hota to default chain exectue hota hai

#RunnableLambda ik lambda function ko runnable main convert krta hai, jiska matlab hai ke aap ek simple function likh sakte hain jo input leta hai aur output deta hai, aur us function ko RunnableLambda ke through ek runnable chain main use kar sakte hain. Iska fayda ye hai ke aap apne custom logic ko easily integrate kar sakte hain apne chains main bina kisi complex setup ke.

branch_chain = RunnableBranch(
    (lambda x : x.sentiment == "positive", prompt2 | model | parser),
    (lambda x : x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "Sorry, I am not sure how to respond to this feedback.")
)

chain = classifier_chain | branch_chain

print(chain.invoke({"feedback": "What a beautiful product!"}))


chain.get_graph().print_ascii()