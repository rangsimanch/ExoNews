
# app/services/ai_processor.py

from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..crud import get_news_ai_by_guid, create_news_ai
from .. import models
from .ai_summarizer import summarize_news

def process_ai_news():
    db: Session = SessionLocal()
    # ดึงข่าวจาก news_rss ที่ยังไม่มีใน news_ai
    news_list = db.query(models.NewsRSS).all()
    for news in news_list:
        if not get_news_ai_by_guid(db, news.guid):
            if news.article:
                # สร้าง JSON ที่จะส่งไปยัง summarize_news
                news_data = {
                    'title': news.title,
                    'published': news.published,
                    'source': news.source,
                    'article': news.article
                }
                # สรุปข่าวโดยใช้ AI Assistants
                summary = summarize_news(news_data)
                if summary:
                    # เพิ่มข้อมูลที่จำเป็น
                    summary['guid'] = news.guid
                    summary['image'] = news.image
                    summary['source'] = news.source
                    summary['release_date'] = news.published

                    # บันทึกลงฐานข้อมูล news_ai
                    news_ai_create = {
                        'guid': summary['guid'],
                        'data': summary,
                    }
                    create_news_ai(db, news_ai_create)
                    print(f"Saved summarized news: {summary['title'].get('en', summary['title'])}")
                else:
                    print(f"Failed to summarize news: {news.title}")
            else:
                print(f"No article content for news: {news.title}")
        else:
            print(f"News already summarized: {news.title}")
    db.close()