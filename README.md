# Healthcare QA System 

## Overview

This project provides an AI-powered healthcare question and answer system built using the **Retrieval-Augmented Generation (RAG)** technique. It leverages the **MedQuAD dataset**, **LangChain**, **HuggingFace embeddings**, **FAISS**, and **DeepSeek R1** to deliver accurate, context-aware medical answers. The system is deployed on **Hugging Face Spaces** using **Streamlit** for a seamless user interface.

## Graphical Representation of RAG System

![RAG System](https://huggingface.co/spaces/Sheryar1998/HealthCare_QA_System/resolve/main/330175374-3543b5ea-3ef5-4fcf-a225-69c.png)

## Features

- **Accurate Healthcare Answers**: The system uses the state-of-the-art **DeepSeek R1** model to generate precise responses.
- **Dynamic Retrieval**: Using **FAISS** and **Maximal Marginal Relevance (MMR)**, the system retrieves diverse and relevant information from the dataset.
- **Intuitive UI**: The user interface is developed with **Streamlit**, offering an easy and responsive way to ask healthcare-related questions.
- **Real-Time Recommendations**: The system uses a **RAG** approach to combine retrieval and generative models for real-time question answering.

## Features

- **Accurate Healthcare Answers**: The system uses the state-of-the-art **DeepSeek R1** model to generate precise responses.
- **Dynamic Retrieval**: Using **FAISS** and **Maximal Marginal Relevance (MMR)**, the system retrieves diverse and relevant information from the dataset.
- **Intuitive UI**: The user interface is developed with **Streamlit**, offering an easy and responsive way to ask healthcare-related questions.
- **Real-Time Recommendations**: The system uses a **RAG** approach to combine retrieval and generative models for real-time question answering.

## How It Works

- **Dataset**: The system uses the **MedQuAD dataset**, which includes medical questions and expert answers.
- **Preprocessing**: The dataset is split into smaller chunks using the **LangChain text splitter** to make it easier to process.
- **Embedding Generation**: The system uses the **HuggingFace model** (`sentence-transformers/all-mpnet-base-v2`) to create embeddings for the medical texts.
- **Vector Store**: These embeddings are stored in a **FAISS vector store** to enable fast and efficient retrieval.
- **Retriever Configuration**: The retrieval process is configured to prioritize diversity and relevance using **Maximal Marginal Relevance (MMR)**.
- **Question Answering**: The system generates answers using the **DeepSeek R1** model with prompt engineering for healthcare-related queries.
- **Deployment**: The entire solution is deployed on **Hugging Face Spaces** with **Streamlit** providing a smooth user experience.


## APP Screenshot

![RAG System](https://huggingface.co/spaces/Sheryar1998/HealthCare_QA_System/resolve/main/qa-system-screenshot.PNG)

**Live Demo**: [Hugging Face Space](https://sheryar1998-healthcare-qa-system.hf.space)


## How to Use

1. Visit the **Hugging Face Space** link provided above.
2. Enter a healthcare-related question in the input box.
3. Press the "Get Answer" button to receive the most relevant answer based on the dataset.

## Future Improvements

- **Expand the dataset**: Integrating additional healthcare-related data for more diverse answers.
- **Better fine-tuning**: Further fine-tuning the **DeepSeek R1** model on domain-specific queries.
- **Multi-language support**: Adding multi-language capabilities to broaden accessibility.
- **Advanced User Interaction**: Implementing features such as voice input for a more interactive experience.

## License

This project is licensed under the **MIT License**.

## Contact

For further inquiries or contact, please reach out to: [sheryarloadhi789@gmail.com](mailto:sheryarloadhi789@gmail.com)

