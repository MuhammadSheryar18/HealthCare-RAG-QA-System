import streamlit as st
import os
import requests
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings  # ✅ Correct import
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFaceHub
from huggingface_hub import model_info
from tenacity import retry, stop_after_attempt, wait_exponential

# --- Vector Store Loading ---
def load_vector_store():
    INDEX_FAISS_PATH = "index.faiss"
    INDEX_PKL_PATH = "index.pkl"
    EMBEDDINGS_PATH = "embeddings.pkl"

    def files_exist():
        return all(os.path.exists(path) for path in [INDEX_FAISS_PATH, INDEX_PKL_PATH, EMBEDDINGS_PATH])

    if not files_exist():
        st.info("Downloading vector store files...")
        FILE_URLS = {
            INDEX_FAISS_PATH: "https://huggingface.co/spaces/Sheryar1998/HealthCare_QA_System/resolve/main/index.faiss",
            INDEX_PKL_PATH: "https://huggingface.co/spaces/Sheryar1998/HealthCare_QA_System/resolve/main/index.pkl",
            EMBEDDINGS_PATH: "https://huggingface.co/spaces/Sheryar1998/HealthCare_QA_System/resolve/main/embeddings.pkl",
        }
        for file, url in FILE_URLS.items():
            if not os.path.exists(file):
                response = requests.get(url, stream=True)
                with open(file, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                st.success(f"Downloaded {file} successfully!")
    
    # Add logging here to verify if the vector store is properly loaded
    try:
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-mpnet-base-v2"
        )
        vector_store = FAISS.load_local(".", embeddings, allow_dangerous_deserialization=True)
        return vector_store
    except Exception as e:
        st.error(f"❌ Failed to load FAISS vector store: {e}")
        st.stop()

# --- Streamlit UI ---
st.set_page_config(page_title="Healthcare AI Assistant", page_icon="💡")

# Updated CSS for logo sizing
st.markdown("""
    <style>
        .header {
            display: flex;
            align-items: center;
            margin-bottom: 30px;
        }
        .logo {
            width: 40px;
            height: auto;
            margin-right: 15px;
        }
        .title {
            color: #2d3436;
            font-size: 28px;
            margin: 0;
        }
        .subtitle {
            color: #636e72;
            font-size: 18px;
            margin-bottom: 30px;
            text-align: center;
        }
        .chat-container {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            margin: 15px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .user-question {
            color: #2d3436;
            font-weight: 600;
            margin-bottom: 10px;
        }
        .ai-answer {
            color: #2d3436;
            line-height: 1.6;
            white-space: pre-wrap;
        }
    </style>
""", unsafe_allow_html=True)

# Header with adjusted logo
st.markdown("""
    <div class="header">
        <img src='https://huggingface.co/spaces/Sheryar1998/HealthCare_QA_System/resolve/main/pngwing.com.png' class='logo'>
        <h1 class="title">Healthcare AI Assistant</h1>
    </div>
    <div class="subtitle">
        Ask questions related to healthcare, and I will provide answers based on available medical knowledge.<br>
        🧠 How may we help you?
    </div>
""", unsafe_allow_html=True)

# --- QA System ---
def main():
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    if not HUGGINGFACE_API_KEY:
        st.error("❌ Missing Hugging Face API Token!")
        st.stop()

    # Initialize LLM first
    llm = HuggingFaceHub(
        repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
        huggingfacehub_api_token=HUGGINGFACE_API_KEY,
        model_kwargs={
            "temperature": 0.01,
            "max_length": 512,
            "timeout": 30
        }
    )

    vector_store = load_vector_store()

    # Optimized retriever configuration
    retriever = vector_store.as_retriever(
        search_type="similarity",  # Use 'similarity' instead of 'dense'
        search_kwargs={
            "k": 5,  # Number of documents to return for the query
            "fetch_k": 20,  # More candidates for better results
            "lambda_mult": 0.7  # Adjust to fine-tune relevance
        }
    )




    
    # Simplified prompt template
    prompt_template = """You have access to the following medical knowledge:
    {context}
    Given the question below, provide the best possible answer.
    If you don't find any relevant information in the context, say: "Not found in medical records."
    
    Question: {question}
    Answer:
    """

    QA_PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    # Use 'stuff' chain type instead of 'refine'
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": QA_PROMPT},
        return_source_documents=False
    )

    # Query handling
    query = st.text_input("Enter your healthcare-related question:", 
                        placeholder="")
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=15))
    def safe_qa_invoke(query):
        return qa.invoke({"query": query})

    if st.button("Get Answer"):
        if not query:
            st.warning("Please enter a question")
        else:
            with st.spinner("Analyzing medical knowledge..."):
                try:
                    result = safe_qa_invoke(query)
                    raw_answer = result["result"]
                    
                    # Improved answer validation
                    if "ANSWER:" in raw_answer:
                        answer_text = raw_answer.split("ANSWER:")[-1].strip()
                        formatted_answer = f"ANSWER: {answer_text}"
                    else:
                        formatted_answer = "Not found in medical records"

                    st.markdown(f"""
                        <div class="chat-container">
                            <div class="user-question">❓ {query}</div>
                            <div class="ai-answer">💡 {formatted_answer}</div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    main()