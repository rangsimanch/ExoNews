
# app/services/ai_summarizer.py

import os
import time
import json
from openai import OpenAI
from ..config import settings

def summarize_news(news_data):
    # สร้างคลาส OpenAI
    client = OpenAI()
    client.api_key = settings.OPENAI_API_KEY

    assistant_id = settings.ASSISTANT_ID  # assistant_id ของคุณ

    # สร้าง thread ใหม่
    thread = client.beta.threads.create()

    # เพิ่มข้อความลงใน thread โดยส่งข้อมูลข่าวในรูปแบบ JSON
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=json.dumps(news_data)
    )

    # รัน assistant
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )

    # รอให้การทำงานเสร็จสิ้น
    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run.status == "completed":
            break
        time.sleep(1)  # ปรับเวลาตามความเหมาะสม

    # ดึงข้อความที่ตอบกลับจาก assistant
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    for msg in messages.data:
        if msg.role == "assistant":
            # สมมติว่าการตอบกลับเป็นข้อความ JSON ที่ต้องการ
            try:
                summary_json = json.loads(msg.content[0].text.value)
                return summary_json
            except (ValueError, AttributeError) as e:
                print(f"Failed to parse assistant's response: {e}")
                return None
    return None