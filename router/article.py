from fastapi import APIRouter, Depends
from schemas import ArticleBase, ArticleDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from typing import List
from db import db_article

router = APIRouter(
    prefix='/article',
    tags=['article']
)

# Create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)

# Get a article
@router.get("/{id}", response_model=ArticleDisplay)
def get_a_article(id: int, db: Session = Depends(get_db)):
    return db_article.get_article(db, id)