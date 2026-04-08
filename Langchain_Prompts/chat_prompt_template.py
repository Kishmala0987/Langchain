from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert.'),
    ('human', 'Tell me about {topic}')
])
prompt = template.invoke({'domain': 'Tour guide', 'topic': 'Istanbul'})
print(prompt)