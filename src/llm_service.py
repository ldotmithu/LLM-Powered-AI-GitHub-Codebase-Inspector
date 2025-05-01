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

def llm_summary(repo, max_repo_chars=2000):
    truncated_repo = repo[:max_repo_chars] if len(repo) > max_repo_chars else repo
    
    prompt = (
        "You are a senior software engineer. Summarize the purpose and functionality "
        "of the following software project in exactly 5 concise bullet points. "
        "Focus on:\n"
        "- Main purpose/value proposition\n"
        "- Core functionality\n"
        "- Key technologies/languages\n"
        "- Architectural approach\n"
        "- Notable features\n\n"
        "Project details:\n"
        f"{truncated_repo}\n\n"
        "Provide only the 5 bullet points, no additional commentary."
    )
    
    response = client.chat.completions.create(
        model="gemma-2b-it",
        messages=[{
            "role": "user",  
            "content": prompt
        }],
        temperature=0.3,  
        max_tokens=500    
    )
    return response.choices[0].message.content

def llm_chain(vecter_db):
    qa_chain = RetrievalQA.from_chain_type(llm=chat_llm,retriever =vecter_db.as_retriever())
    return qa_chain
