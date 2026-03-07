#Semantic Search & Query Clustering API
This project implements a semantic search and query clustering system with an API interface built using FastAPI.
The system groups semantically similar queries into clusters and exposes an API endpoint for interacting with the trained model.
The project demonstrates:
1.Semantic query clustering
2.Model training and batch inference
3.API deployment
4.Visualization of clusters
5.Integration of ML workflow with an API service



#Project Workflow
The overall system flow is shown below.
User Query / Dataset
        │
        ▼
Text Preprocessing
        │
        ▼
Embedding Generation
        │
        ▼
Semantic Clustering
        │
        ▼
Model Training
        │
        ▼
Batch Output Generation
        │
        ▼
FastAPI Service
        │
        ▼
API Endpoint for Query Processing



#Running the API
The API server is built using FastAPI and served with Uvicorn.
Start the server:
uvicorn main:app --reload --port 8001
API runs at:
http://127.0.0.1:8001



#API Status
Below is the API running successfully.
server running on 127.0.0.1:8001
application startup logs
request handling



#Model Training
The model training process is implemented in:
environment.ipynb
The training pipeline performs:
1.Data loading
2.Text preprocessing
3.Embedding generation
4.Semantic clustering
5.Model output generation



#Semantic Cluster Visualization
The clustering results are visualized in the notebook.
These graphs show how semantically similar queries are grouped together.
The visualization demonstrates:
->grouping of related queries
->separation between clusters
->structure of the semantic search space



#Project Screenshots Section
You can organize screenshots like this:
screenshots/
│
├── api_running.jpeg
├── semantic_clusters.jpeg
├── training_output.jpeg
└── terminal_execution.jpeg



#Technologies Used
1.Python
2.FastAPI
3.Uvicorn
4.Jupyter Notebook
5.Machine Learning libraries for clustering and embeddings



#Key Features
->Semantic query clustering
->Visualization of cluster structures
->Model training and batch inference
->API integration with ML model
->End-to-end ML pipeline demonstration



#Conclusion
This project demonstrates how semantic embeddings and clustering techniques can be used to group related queries and expose the functionality through a production-style API.
The integration of model training, visualization, and API deployment illustrates a practical workflow for building ML-powered backend services.