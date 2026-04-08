from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name= 'chat_history'), # This is where the chat history will be inserted 
    ('human', '{query}')
])
chat_history = []

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)
prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'Where is my refund?'})
print(prompt)