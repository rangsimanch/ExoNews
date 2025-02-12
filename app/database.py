
# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# สร้าง engine สำหรับเชื่อมต่อกับฐานข้อมูล
engine = create_engine(settings.DATABASE_URL)

# สร้าง SessionLocal สำหรับการใช้งานฐานข้อมูล
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# สร้าง Base สำหรับโมเดล
Base = declarative_base()