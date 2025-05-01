from groq import Groq
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationalRetrievalChain
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
    "🧑‍💻 You are a senior software engineer tasked with summarizing a software project.\n\n"
    "🎯 **Objective:** Provide a concise summary (max 250 words) explaining the *purpose* and *functionality* of the project.\n\n"
    "📌 **Include:**\n"
    "- ✅ Main features\n"
    "- 🛠️ Technologies used (in `<code>` format)\n"
    "- 🏗️ Overall architecture (brief)\n\n"
    "✨ **Style Guidelines:**\n"
    "- Use emojis for clarity and engagement\n"
    "- Keep the explanation beginner-friendly and easy to understand\n"
    "- Follow a friendly, clear tone\n\n"
    f"📄 **Project Excerpt:**\n{repo}"
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
    qa_chain = RetrievalQA.from_chain_type(
        llm=chat_llm,
        retriever=vector_db.as_retriever(),
        chain_type="stuff",
        return_source_documents=False
    )

    return qa_chain
# def llm_chain(vector_db):
#     memory = ConversationSummaryMemory(llm=chat_llm, memory_key = "chat_history", return_messages=True)
#     qa_chain = ConversationalRetrievalChain.from_llm(chat_llm, retriever=vector_db.as_retriever(search_type="mmr", search_kwargs={"k":8}), memory=memory)
#     return qa_chain
    



