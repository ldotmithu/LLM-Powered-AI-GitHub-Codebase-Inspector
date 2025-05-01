from groq import Groq
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os 
load_dotenv()

client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)

chat_llm = ChatGroq(
    api_key=os.environ["GROQ_API_KEY"],
    temperature=0.6,
    model="llama3-70b-8192"
)

def llm_summary(repo, max_repo_chars=2000):
    #truncated_repo = repo[:max_repo_chars] if len(repo) > max_repo_chars else repo
    
    prompt = (
        "You are a senior software engineer. Summarize the purpose and functionality "
        "Highlight its main features, technologies used, and overall architecture.\n\n"
        "Easy way to explain about the project"

    "Guidelines:\n"
    "- Use emojis as shown for visual scanning\n"
    "- Format technologies as code tags\n"
    
    "Project excerpt:\n"
    f"{repo}"
)
    
    response = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[{
            "role": "user",  
            "content": prompt
        }],
        temperature=0.9,  
        #max_tokens=500,
        response_format={"type": "text"}    
    )
    return response.choices[0].message.content

def llm_chain(vector_db):
    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a helpful AI assistant. Use the information below to answer the user's question in accurate way.

Only use the context provided. If the answer is not in the context, say: "I'm not sure based on the provided code."

Context:
{context}

Question:
{question}

Answer (clear and simple):
"""
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=chat_llm,
        retriever=vector_db.as_retriever(),
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt_template},
        return_source_documents=False
    )

    return qa_chain



