
# app/services/news_fetcher.py

import feedparser
from newspaper import Article
from ..config import settings

def fetch_news():
    news_items = []
    for feed_url in settings.RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            news = {
                'guid': entry.id,
                'title': entry.title,
                'link': entry.link,
                'published': entry.published,
                'summary': entry.summary,
                'source': feed.feed.title,
                'image': entry.media_content[0]['url'] if 'media_content' in entry else None
            }
            
            # ดึงเนื้อหาข่าวโดยใช้ newspaper3k
            try:
                article = Article(news['link'])
                article.download()
                article.parse()
                news['article'] = article.text  # เพิ่มเนื้อหาข่าวลงใน news entry
            except Exception as e:
                print(f"Failed to retrieve article content for {news['link']}: {e}")
                news['article'] = None  # กำหนดค่าเป็น None หากดึงเนื้อหาไม่ได้
            
            news_items.append(news)
    return news_items