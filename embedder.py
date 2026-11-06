# embedder.py
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from data_loader import load_data

def build_vectorstore():
    print("📥 Loading data from MongoDB...")
    texts = load_data()
    print(f"📄 Got {len(texts)} texts from MongoDB")

    if not texts or len(texts) == 0:
        print("❌ STOP: MongoDB se 0 texts aaye. FAISS nahi bana raha.")
        print("👉 Pehle data_loader.py / Atlas me collection name check karo.")
        return None

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    docs = splitter.create_documents(texts)
    print(f"✂️ Made {len(docs)} chunks")

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-MiniLM-L3-v2"
    )

    vectorstore = FAISS.from_documents(docs, embedding_model)
    vectorstore.save_local("vectorstore")
    print(f"✅ Successfully built FAISS index with {len(docs)} chunks.")
    return vectorstore

# Ye line sabse important hai - import karne pe code nahi chalega
if __name__ == "__main__":
    build_vectorstore()