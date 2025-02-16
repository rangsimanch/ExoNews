
# app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

# สำหรับ news_rss
def get_news_rss_by_guid(db: Session, guid: str):
    return db.query(models.NewsRSS).filter(models.NewsRSS.guid == guid).first()

def create_news_rss(db: Session, news: schemas.NewsRSSCreate):
    db_news = models.NewsRSS(**news.model_dump(), created_at=datetime.now())
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

# สำหรับ news_ai
def get_news_ai_by_guid(db: Session, guid: str):
    return db.query(models.NewsAI).filter(models.NewsAI.guid == guid).first()
def create_news_ai(db: Session, news_ai: schemas.NewsAICreate):
    db_news_ai = models.NewsAI(**news_ai.model_dump(), created_at=datetime.now())
    db.add(db_news_ai)
    db.commit()
    db.refresh(db_news_ai)
    return db_news_ai