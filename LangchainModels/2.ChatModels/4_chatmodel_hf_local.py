from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFacePipeline(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
    pipeline_kwargs = dict(
        max_new_tokens = 100,
        temperature = 0.7,
    )
)

llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of Pakistan?")
print(result.content)