# app/main.py

from fastapi import FastAPI
from .database import engine
from .models import Base
from .services.scheduler import start_scheduler

# สร้างแอปพลิเคชัน FastAPI
app = FastAPI()

# สร้างตารางฐานข้อมูลตามโมเดลที่กำหนด ถ้ายังไม่มี
Base.metadata.create_all(bind=engine)

# เริ่มต้น Scheduler
start_scheduler()

# เส้นทางหลัก
@app.get("/")
def read_root():
    return {"message": "Microservice A is running"}