# 🚀 AI-Powered Job Search Assistant

## 📌 Overview  
Finding the right job can be overwhelming, with thousands of job listings to filter through. This AI-powered job search assistant simplifies the process by leveraging **Natural Language Processing (NLP)** and **Similarity Search** to match users with the most relevant job opportunities based on their skills, experience, and location.

## 🛠 Technologies Used  
- **Python** 🐍  
- **Hugging Face Datasets** 📚 (Fetching job descriptions)  
- **Sentence-BERT** 🔍 (Generating job and query embeddings)  
- **FAISS (Facebook AI Similarity Search)** ⚡ (Fast retrieval of relevant jobs)  
- **Gradio** 🎨 (User-friendly interactive interface)  

## ⚙️ How It Works  
1. **Data Extraction:** Job descriptions are fetched from [Hugging Face Dataset](https://huggingface.co/datasets/cnamuangtoun/resume-job-description-fit).  
2. **Embedding Generation:** Job descriptions are converted into embeddings using **Sentence-BERT**.  
3. **Storing Embeddings:** The embeddings are stored in **FAISS** for quick similarity search.  
4. **Query Processing:** The user’s job search input is also converted into an embedding and compared with stored job descriptions.  
5. **Job Matching:** The system retrieves and ranks the most relevant job listings based on similarity.  
6. **Interactive UI:** Users can enter job preferences in a **Gradio-based interface**, and the system instantly recommends job matches.

## 🎯 Example Usage  
A user enters:  
💬 *“I have three years of experience in Python and SQL and am looking for a job in New York.”*  

📌 The system processes the input, searches FAISS for relevant jobs, and returns the **best-matching job postings** in an easy-to-use Gradio UI.

## 🏗️ Installation & Setup  
### 🔹 Prerequisites  
Make sure you have the following installed:  
- Python 3.8+  
- Pip  
- Git  

### 🔹 Clone the Repository  
```bash
git clone https://github.com/yourusername/AI-Job-Search-Assistant.git
cd AI-Job-Search-Assistant
