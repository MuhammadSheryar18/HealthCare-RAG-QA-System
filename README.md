# Healthcare AI Assistant 🤖💊

![App Screenshot](https://huggingface.co/spaces/Sheryar1998/HealthCare_QA_System/assets/qa-system-screenshot.PNG)  
*Replace with your actual screenshot URL*

## Overview
A Retrieval Augmented Generation (RAG) system for medical question answering, powered by DeepSeek LLM and FAISS vector search. This system provides evidence-based answers to healthcare questions using the MedQuad dataset and is deployed as an interactive web app via Streamlit.

**Live Demo**: [Hugging Face Space](https://sheryar1998-healthcare-qa-system.hf.space)

## Features ✨
- Natural language processing for medical queries
- Context-aware answer generation
- Hybrid search (MMR) with FAISS vector store
- Streamlit web interface with medical UI theme
- Hugging Face model integration

## How It Works 🧪
```mermaid
graph TD
    A[User Input Question] --> B{Check Vector Store Files}
    B -->|Files Exist| C[Load FAISS Vector Store]
    B -->|Files Missing| D[Download from Hugging Face]
    D --> C
    C --> E[Initialize HuggingFace Embeddings]
    E --> F["Configure Retriever<br/>(search_type: similarity, k:5)"]
    F --> G["Initialize DeepSeek LLM<br/>(temp:0.01, max_len:512)"]
    G --> H[Create QA Prompt Template]
    H --> I["Build RetrievalQA Chain<br/>(chain_type: stuff)"]
    I --> J[Submit Query]
    J --> K{Valid Question?}
    K -->|Yes| L[Retrieve Context+Generate Answer]
    K -->|No| M[Show Warning]
    L --> N{Found in Context?}
    N -->|Yes| O[Format Answer with Prefix]
    N -->|No| P["Return 'Not found'"]
    O --> Q[Display Styled Response]
    P --> Q
    M --> R[End Session]
    
    style B fill:#ffebcc,stroke:#f0ad4e
    style F fill:#d4edda,stroke:#28a745
    style G fill:#d1ecf1,stroke:#17a2b8
    style H fill:#f8d7da,stroke:#dc3545
    style Q fill:#e2e3e5,stroke:#6c757d
