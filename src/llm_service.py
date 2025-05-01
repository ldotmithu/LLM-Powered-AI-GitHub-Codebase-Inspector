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
    #truncated_repo = repo[:max_repo_chars] if len(repo) > max_repo_chars else repo
    
    prompt = (
    "Create an engaging yet professional project summary formatted as markdown. "
    "Use exactly 5 bullet points with this structure:\n\n"
    
    "✨ **Purpose**: <1-sentence value proposition>\n\n"
    "🚀 **Core Functionality**: <2-3 key capabilities in simple terms>\n\n"
    "🛠️ **Tech Stack**: <main languages/frameworks as tags, e.g. `Python` `React`>\n\n"
    "🏛️ **Architecture**: <high-level design pattern in 1 phrase + key detail>\n\n"
    "🌟 **Special Sauce**: <what makes this project unique or innovative>\n\n"
    
    "Guidelines:\n"
    "- Use emojis as shown for visual scanning\n"
    "- Keep each point under 15 words\n"
    "- Format technologies as code tags\n"
    "- Make it accessible to both technical and non-technical readers\n\n"
    
    "Project excerpt:\n"
    f"{repo}"
)
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",  
            "content": prompt
        }],
        temperature=0.9,  
        #max_tokens=500,
        response_format={"type": "text"}    
    )
    return response.choices[0].message.content

def llm_chain(vecter_db):
    qa_chain = RetrievalQA.from_chain_type(llm=chat_llm,retriever =vecter_db.as_retriever())
    return qa_chain
