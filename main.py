from openai import OpenAI
import os
import requests

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

prompt = """
生成今日全球投资增强版早报：

1. 国际时政
2. AI行业
3. 电商
4. Fintech
5. 中国市场
6. 东南亚市场
7. 产品机会
8. 投资机会
9. 风险雷达

全部表格输出
"""

response = client.responses.create(
    model="gpt-5.5",
    input=prompt
)

report = response.output_text

requests.post(
    f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendMessage",
    json={
        "chat_id": os.getenv("TELEGRAM_CHAT_ID"),
        "text": report[:4000]
    }
)
