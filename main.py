import streamlit as st
from src.helper import load_github_url, split_repo, load_embedding, vector_db
from src.llm_service import llm_summary, llm_chain

# Page configuration for a clean layout
st.set_page_config(page_title="LLM GitHub Codebase Inspector", layout="wide")

# Title and description for the main page
st.title("🧠 LLM-Powered AI GitHub Codebase Inspector")
st.markdown(
    """
    Unlock the power of AI to analyze and understand GitHub repositories! 🔍  
    Use advanced language models to extract project summaries and get answers to specific questions about the codebase.  
    Simply paste your GitHub repository URL below and let the AI break it down for you. 🚀
    """
)

# Sidebar for user controls
st.sidebar.title("Project Controls")
url = st.sidebar.text_input("🔗 Enter the GitHub Repository URL")

# Placeholder for dynamic status updates in the sidebar
status_box = st.sidebar.empty()

# Core functionality based on user input
if url:
    try:
        # Clone the repo and process the data
        status_box.text("🔄 Cloning the repository...")
        data = load_github_url(repo_url=url)

        status_box.text("🔍 Splitting and chunking the code...")
        docs = split_repo(repo=data)

        status_box.text("🔗 Loading embedding model from Hugging Face...")
        embedding = load_embedding()

        status_box.text("💾 Creating vector store from code chunks...")
        vector = vector_db(embedding=embedding, docs=docs)

        status_box.text("🧠 Generating project summary with LLM...")
        summary = llm_summary(repo=data)

        # Final success message
        status_box.text("✅ Done!")

        # Display project summary
        st.markdown("---")
        st.subheader("📄 Project Summary")
        #st.markdown(
            #f"<div style='background-color: #2D2D2D; padding: 20px; border-radius: 10px; font-size:16px; color:white;'>{summary}</div>",
            #unsafe_allow_html=True,)
        st.markdown(summary,unsafe_allow_html=True)    

        # Section for users to ask questions about the codebase
        st.markdown("---")
        st.subheader("💬 Ask Questions About the Codebase")
        user_question = st.text_input("Type your question about the codebase...")

        if user_question:
            with st.spinner("💡 Generating answer..."):
                answer = llm_chain(query=user_question, vectorstore=vector)
            st.success("✅ Answer:")
            st.write(answer)

    except Exception as e:
        status_box.text("❌ Error")
        st.error(f"Oops! Something went wrong: {str(e)}")
