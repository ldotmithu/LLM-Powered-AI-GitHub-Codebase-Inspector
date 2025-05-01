from langchain_community.document_loaders.git import GitLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os 
import shutil
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import subprocess

def git_clean_and_delete(repo_path):
    if os.path.exists(repo_path):
        try:
            # Reset any Git changes first
            subprocess.run(["git", "-C", repo_path, "reset", "--hard"], check=True)
            subprocess.run(["git", "-C", repo_path, "clean", "-fd"], check=True)
        except:
            pass  # Ignore if not a Git repo
        shutil.rmtree(repo_path, ignore_errors=True)



def load_github_url(repo_url):
    if os.path.exists("test_repo"):
        git_clean_and_delete("test_repo")
        
    loader = GitLoader(
        repo_path="test_repo",
        clone_url=repo_url,
        file_filter=lambda f: f.endswith((".py", ".js", ".ts", ".java", ".cpp", ".md"))
    )
    repo = loader.load()
    git_clean_and_delete("test_repo")

    return repo


def split_repo(repo):
    splittter = RecursiveCharacterTextSplitter(chunk_size = 1000,
                                   chunk_overlap=100)
    docs = splittter.split_documents(repo)
    return docs

def load_embedding():
    embedding = HuggingFaceEmbeddings()
    return embedding

def vector_db(embedding,docs):
    vectors_db= FAISS.from_documents(documents=docs,embedding=embedding)
    return vectors_db


    

