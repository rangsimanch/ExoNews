
# ใช้ภาพ Python เวอร์ชันล่าสุด
FROM python:3.9-slim

# ตั้งค่าตัวแปรสภาพแวดล้อม
ENV PYTHONUNBUFFERED 1

# สร้างไดเรกทอรีสำหรับแอปพลิเคชัน
WORKDIR /app

# คัดลอกไฟล์ requirements.txt และติดตั้งไลบรารี
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ดทั้งหมดไปยังภาพ Docker
COPY . /app

# เปิดพอร์ตที่ใช้โดย Uvicorn
EXPOSE 8000

# คำสั่งในการรันแอปพลิเคชัน
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]