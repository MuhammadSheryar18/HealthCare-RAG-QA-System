# Healthcare AI Assistant 🤖💊


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
    A[User Query] --> B[Load Medical CSV Data]
    B --> C[Split Documents<br>chunk_size=2000]
    C --> D[Generate Embeddings<br>all-mpnet-base-v2]
    D --> E[FAISS Vector Store]
    E --> F[MMR Retriever<br>k=15, λ=0.5]
    F --> G[DeepSeek LLM<br>temp=0.01]
    G --> H[Generate Answer]
    
    style A fill:#e8f5e9,stroke:#81c784
    style B fill:#fff3e0,stroke:#ffb74d
    style C fill:#e3f2fd,stroke:#64b5f6
    style D fill:#f3e5f5,stroke:#ba68c8
    style E fill:#ffebee,stroke:#e57373
    style F fill:#f0f4c3,stroke:#dce775
    style G fill:#c8e6c9,stroke:#81c784
    style H fill:#b2dfdb,stroke:#4db6ac
