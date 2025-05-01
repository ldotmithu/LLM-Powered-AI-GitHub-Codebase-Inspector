from groq import Groq
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os 
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

chat_llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.6,
    model="mistral-saba-24b"
)

def llm_summery(repo):
    prompt = (
        "You are a senior software engineer. Summarize the purpose and functionality "
        "of the following software project in exactly 5 concise bullet points. "
        "Highlight its main features, technologies used, and overall architecture.\n\n"
        f"{repo}")
    
    response = client.chat.completions.create(
        messages=[{
            "role":'system',
            'content':prompt
        }],model="gemma2-9b-it",
        temperature=0.5
    )
    return response.choices[0].message.content

def llm_chain(vecter_db):
    qa_chain = RetrievalQA.from_chain_type(llm=chat_llm,retriever =vecter_db.as_retriever())
    return qa_chain
