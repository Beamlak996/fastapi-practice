from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/hell0")
def index():
    return {"message": "Hello World"}

@app.get("/blog/all")
def get_all_blogs(page=1, page_size:Optional[int] = None):
    return {'message': f"All {page_size} blogs on page {page}."}
