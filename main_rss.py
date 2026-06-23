import os
import requests

message = """
RSS测试版

GitHub Actions
RSS流程
Telegram推送

全部正常
"""

requests.post(
    f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendMessage",
    json={
        "chat_id": os.getenv('TELEGRAM_CHAT_ID'),
        "text": message
    }
)
