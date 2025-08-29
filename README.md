# 🎬 Zymr Movie API Assignment

A simple **Movie API** built with [FastAPI].  
It demonstrates how to design and implement **CRUD operations** with request/response validation, in-memory storage, unit testing, and auto-generated documentation (OpenAPI 3.0 + Swagger UI + ReDoc).

 Tech Stack

- **FastAPI** → Modern Python framework for APIs (with auto docs)  
- **Uvicorn** → server for running FastAPI  
- **Pydantic** → Data validation 
- **Pytest** → Testing framework for verifying API endpoints  


## ▶How to Run the Project

1. **Clone the repo**:
   git clone https://github.com/prakhar1507/zymr_movie_api_assignment.git
   cd zymr_movie_api_assignment

2. Create virtual environment & activate:
   
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux

3.Install dependencies:
pip install -r requirements.txt


To run unit tests:
pytest -v


4.Start the server:
uvicorn app.main:app --reload



API Documentation
FastAPI auto-generates OpenAPI 3.0 docs:
Swagger UI → http://127.0.0.1:8000/docs
ReDoc → http://127.0.0.1:8000/redoc
