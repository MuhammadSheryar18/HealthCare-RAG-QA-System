# Healthcare AI Assistant 🤖💊

![App Screenshot](https://huggingface.co/spaces/Sheryar1998/HealthCare_QA_System/resolve/main/app-screenshot.png)  
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
graph LR
A[User Question] --> B(FAISS Vector Search)
B --> C{Context Matching}
C -->|Found| D[Generate Answer]
C -->|Not Found| E[Fallback Response]
D --> F[Display Answer]
