# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

# นำเข้า SessionLocal และ engine จาก database.py
from .database import SessionLocal, engine
# นำเข้าโมเดลหลักและโมเดลสำหรับตาราง news_ai
from .models import Base, NewsAI
# นำเข้า Pydantic Schema ของ NewsAI
from .schemas import NewsAI as NewsAISchema

from .services.scheduler import start_scheduler

app = FastAPI()
start_scheduler()

# สร้างตารางฐานข้อมูลตามโมเดล (ถ้ายังไม่มี)
Base.metadata.create_all(bind=engine)

# ฟังก์ชัน generator สำหรับสร้าง/ปิด Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Microservice A is running"}

# Endpoint สำหรับดึงข้อมูลจากตาราง news_ai ในรูปแบบ JSON
@app.get("/NewsAI", response_model=List[NewsAISchema])
def read_news_ai(db: Session = Depends(get_db)):
    news_ai_data = db.query(NewsAI).all()
    return news_ai_data