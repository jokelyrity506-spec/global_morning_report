import os
import requests

message = """
测试成功

GitHub Actions 已运行
Telegram 已连接
"""

requests.post(
    f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendMessage",
    json={
        "chat_id": os.getenv("TELEGRAM_CHAT_ID"),
        "text": message
    }
)
