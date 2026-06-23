import os
import feedparser
import requests
from datetime import datetime

RSS_FEEDS = {

    "🌍 全球热点":
    "https://feeds.reuters.com/reuters/topNews",

    "🤖 AI":
    "https://techcrunch.com/category/artificial-intelligence/feed/",

    "💻 科技":
    "https://www.theverge.com/rss/index.xml",

    "🌏 东南亚":
    "https://www.techinasia.com/feed",

    "💳 Fintech":
    "https://www.finextra.com/rss/headlines.aspx",

}

today = datetime.utcnow().strftime("%Y-%m-%d")

report = f"""
🌏 全球投资增强版早报

日期：{today}

========================

"""

for category, url in RSS_FEEDS.items():

    report += f"\n{category}\n"

    try:

        feed = feedparser.parse(url)

        for item in feed.entries[:5]:

            title = item.title.strip()

            report += f"• {title}\n"

    except Exception:

        report += "• 获取失败\n"

report += """

========================

📈 产品机会

1. AI客服Agent
2. AI活动运营助手
3. AI积分商城
4. 东南亚返佣平台
5. AI竞品监控系统

========================

💰 投资机会

1. AI基础设施
2. 东南亚Fintech
3. 企业AI SaaS
4. 电商服务商
5. 云计算

========================

⚠ 风险雷达

1. 美联储政策变化
2. 国际油价波动
3. AI估值风险
4. 地缘政治风险
5. 东南亚监管变化

"""

token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

for i in range(0, len(report), 3500):

    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": report[i:i+3500]
        }
    )

print("RSS V2 Report Sent")
