import os
import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

@st.cache_resource
def get_vectorstore():
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-MiniLM-L3-v2"
    )

    if not os.path.exists("vectorstore/index.faiss"):
        print("⚙️ Vectorstore not found. Building from scratch...")
        from embedder import build_vectorstore
        build_vectorstore()  # <- ye call karna zaruri tha
        print("✅ Vectorstore built successfully.")

    vectorstore = FAISS.load_local(
        "vectorstore",
        embedding_model,
        allow_dangerous_deserialization=True
    )
    return vectorstore

def retrieve_docs(query):
    try:
        vectorstore = get_vectorstore()
        docs = vectorstore.max_marginal_relevance_search(query, k=3, fetch_k=10)
    except Exception as e:
        print(f"[retriever] Vectorstore load failed: {e}")
        return ""

    unique_docs = []
    seen = set()
    for doc in docs:
        content = doc.page_content.strip()
        if content and content not in seen:
            seen.add(content)
            unique_docs.append(content)

    return "\n".join(unique_docs[:3])