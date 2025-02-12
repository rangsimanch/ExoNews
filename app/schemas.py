
# app/schemas.py

from pydantic import BaseModel
from datetime import datetime
from typing import Any, Optional

class NewsRSSBase(BaseModel):
    guid: str
    title: str
    link: str
    published: str
    summary: str
    source: str
    image: Optional[str] = None
    article: Optional[str] = None  # เพิ่มฟิลด์ article

class NewsRSSCreate(NewsRSSBase):
    pass

class NewsRSS(NewsRSSBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class NewsAIBase(BaseModel):
    guid: str
    data: Any

class NewsAICreate(NewsAIBase):
    pass

class NewsAI(NewsAIBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True