from openai import OpenAI
import os
import requests

client = OpenAI(
api_key=os.getenv("OPENAI_API_KEY")
)

PROMPT = """
请生成今日全球投资增强版晨报。

要求：

1. 全球热点TOP10
2. 国际时政
3. AI行业
4. 中国互联网
5. 东南亚市场
6. Fintech
7. 电商
8. 产品机会（PM Insight）
9. 投资机会（Trade Ideas）
10. 风险雷达（Risk Radar）

要求：

* 表格输出
* 只保留最近24小时重要变化
* 避免重复旧闻
* 内容简洁但信息密度高
  """

def send_telegram(text):
token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

```
for i in range(0, len(text), 3500):
    chunk = text[i:i+3500]

    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": chunk
        },
        timeout=30
    )
```

try:

```
response = client.responses.create(
    model="gpt-5",
    input=PROMPT
)

report = response.output_text

send_telegram(report)

print("Morning report sent successfully")
```

except Exception as e:

```
print(f"Error: {e}")
raise
```
