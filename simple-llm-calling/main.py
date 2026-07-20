from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemma-4-31b-it")



prompt = [
    ["system","You are a helpful assistant and will answer questions in one single line."],
    ["user"," How many moons are in the solar system?"]
];

response = llm.invoke(prompt)
print(response.content)