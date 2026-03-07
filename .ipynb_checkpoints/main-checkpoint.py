from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# request schema
class QueryRequest(BaseModel):
    query: str

# simple cache
cache = {}

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/about")
def about():
    return {"message": "Semantic Search Cache API"}

@app.post("/query")
def query(request: QueryRequest):

    if request.query in cache:
        return {
            "source": "cache",
            "result": cache[request.query]
        }

    result = f"Computed result for {request.query}"

    cache[request.query] = result

    return {
        "source": "computed",
        "result": result
    }