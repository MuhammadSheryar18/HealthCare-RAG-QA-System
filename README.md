# Healthcare AI Assistant 🤖💊

## Preview
![Alt Text](https://raw.githubusercontent.com/Sheryar1998/HealthCare_QA_System/main/assets/your-image-name.png)

## Overview
A Retrieval Augmented Generation (RAG) system for medical question answering, powered by DeepSeek LLM and FAISS vector search. This system provides evidence-based answers to healthcare questions using the MedQuad dataset and is deployed as an interactive web app via Streamlit.

**Live Demo**: [Hugging Face Space](https://sheryar1998-healthcare-qa-system.hf.space)

## Features ✨
- Medical QA with evidence-based responses
- FAISS vector search with MMR diversification
- Streamlit web interface with medical UI
- Context-aware answer generation


## Installation 💻
```bash
git clone https://github.com/yourusername/healthcare-qa-rag.git
cd healthcare-qa-rag
pip install -r requirements.txt

## Usage 🏥

### Set Hugging Face Token
```bash
export HUGGINGFACEHUB_API_TOKEN="your_api_token"

## Launch Application 🚀

```bash
streamlit run src/app/app.py
