
# app/services/scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from .rss_processor import process_rss_news
from .ai_processor import process_ai_news

def start_scheduler():
    scheduler = BackgroundScheduler()
    # รัน process_rss_news ทุกๆ 30 นาที
    scheduler.add_job(process_rss_news, 'interval', minutes=30, id='rss_job')
    # รัน process_ai_news ทุกๆ 35 นาที
    scheduler.add_job(process_ai_news, 'interval', minutes=35, id='ai_job')
    scheduler.start()