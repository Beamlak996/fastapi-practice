from fastapi import FastAPI, Request, HTTPException
from router import blog_get
from router import blog_post
from router import user
from router import article
from router import product
from db import models
from db.database import engine
from exceptions import StoryException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)

@app.get("/hell0")
def index():
    return {"message": "Hello World"}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': exc.name}
    )

# @app.exception_handler(HTTPException)
# def custom_handle(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400)



models.Base.metadata.create_all(engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
