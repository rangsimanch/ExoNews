
# app/models.py

from sqlalchemy import Column, Integer, String, JSON, DateTime, Text
from .database import Base

class NewsRSS(Base):
    __tablename__ = "news_rss"

    id = Column(Integer, primary_key=True, index=True)
    guid = Column(String, unique=True, index=True)
    title = Column(String)
    link = Column(String)
    published = Column(String)
    summary = Column(String)
    source = Column(String)
    image = Column(String)
    article = Column(Text)  # ฟิลด์สำหรับเก็บเนื้อหาข่าว
    created_at = Column(DateTime)

class NewsAI(Base):
    __tablename__ = "news_ai"

    id = Column(Integer, primary_key=True, index=True)
    guid = Column(String, unique=True, index=True)
    data = Column(JSON)  # เก็บข้อมูล JSON จาก AI Assistants
    created_at = Column(DateTime)