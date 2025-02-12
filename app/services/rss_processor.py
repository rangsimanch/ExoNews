
# app/services/rss_processor.py

from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..crud import get_news_rss_by_guid, create_news_rss
from .news_fetcher import fetch_news

def process_rss_news():
    db: Session = SessionLocal()
    news_items = fetch_news()
    for news in news_items:
        if not get_news_rss_by_guid(db, news['guid']):
            # เก็บข่าวลงฐานข้อมูล news_rss
            news_create = {
                'guid': news['guid'],
                'title': news['title'],
                'link': news['link'],
                'published': news['published'],
                'summary': news['summary'],
                'source': news['source'],
                'image': news['image'],
                'article': news['article'],  # เก็บเนื้อหาข่าวลงฐานข้อมูล
            }
            create_news_rss(db, news_create)
            print(f"Saved RSS news: {news['title']}")
        else:
            print(f"Duplicate RSS news found: {news['title']}")
    db.close()