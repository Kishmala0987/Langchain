from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)
chat_history = []
while True:
    user_input = input("User: ")
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = llm.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ", result.content)

print(chat_history)