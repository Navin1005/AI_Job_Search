import faiss
import torch
import gradio as gr
from datasets import load_dataset
from sentence_transformers import SentenceTransformer

# Load the dataset from Hugging Face
print("Loading dataset...")
dataset = load_dataset("cnamuangtoun/resume-job-description-fit")

# Extract job descriptions
job_descriptions = [entry["job_description_text"] for entry in dataset["train"]]

print(f"Extracted {len(job_descriptions)} job descriptions.")

# Load the embedding model (Sentence-BERT)
print("Loading embedding model...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Generate embeddings for job descriptions
print("Generating embeddings for job descriptions...")
job_embeddings = model.encode(job_descriptions, convert_to_tensor=True)

# Convert embeddings to numpy for FAISS
job_embeddings_np = job_embeddings.cpu().numpy()

# Create FAISS index for similarity search
dimension = job_embeddings_np.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(job_embeddings_np)

# Function to find job matches based on user query
def find_matching_jobs(user_query, top_k=5):
    # Generate embedding for user query
    query_embedding = model.encode([user_query], convert_to_tensor=True).cpu().numpy()
    
    # Search FAISS index
    distances, indices = index.search(query_embedding, top_k)
    
    # Retrieve matching job descriptions
    results = [job_descriptions[i] for i in indices[0]]
    
    return "\n\n".join([f"{i+1}. {job}" for i, job in enumerate(results)])

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# 🔍 AI-Powered Job Search\nEnter your skills, experience, and location to find relevant jobs.")
    
    user_input = gr.Textbox(label="Enter your job search query", 
                            placeholder="E.g., 'I am skilled in Python and SQL with 3 years of experience. Looking for a job in New York.'")
    
    output = gr.Textbox(label="Matching Job Descriptions")
    
    search_button = gr.Button("Find Jobs")
    search_button.click(find_matching_jobs, inputs=user_input, outputs=output)

print("Starting Gradio UI...")
demo.launch()
