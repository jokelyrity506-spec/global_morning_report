import os
import feedparser
import requests

from googletrans import Translator

translator = Translator()

RSS_FEEDS = {

"🌍 全球热点":
"https://feeds.reuters.com/reuters/topNews",

"📈 宏观经济":
"https://www.cnbc.com/id/100003114/device/rss/rss.html",

"🤖 AI":
"https://techcrunch.com/category/artificial-intelligence/feed/",

"💻 科技互联网":
"https://www.theverge.com/rss/index.xml",

"🔥 芯片":
"https://www.tomshardware.com/feeds/all",

"🤖 机器人":
"https://spectrum.ieee.org/rss/robotics/fulltext",

"⚡ 新能源":
"https://www.energy.gov/rss.xml",

"🚗 汽车":
"https://insideevs.com/rss/news/",

"💳 Fintech":
"https://www.finextra.com/rss/headlines.aspx",

"🪙 稳定币":
"https://cointelegraph.com/rss/tag/stablecoin",

"₿ Crypto":
"https://www.coindesk.com/arc/outboundfeeds/rss/",

"🛒 电商":
"https://www.digitalcommerce360.com/feed/",

"📱 消费电子":
"https://www.engadget.com/rss.xml",

"🏥 医疗健康":
"https://www.medicalnewstoday.com/rss",

"📡 通信网络":
"https://www.lightreading.com/rss_simple.asp",

"🚀 航空航天":
"https://spacenews.com/feed/",

"⛽ 能源":
"https://oilprice.com/rss/main",

"🌏 东南亚":
"https://www.techinasia.com/feed",

"🕌 中东":
"https://www.arabnews.com/rss.xml",

"💰 投融资":
"https://techcrunch.com/category/startups/feed/"
}

report = "🌏 全球投资增强版早报\n\n"

for category, url in RSS_FEEDS.items():

    report += f"\n{category}\n"

    try:

        feed = feedparser.parse(url)

        for item in feed.entries[:5]:

            title_cn = translator.translate(
                item.title,
                dest="zh-cn"
            ).text

            report += f"• {title_cn}\n"

    except Exception:

        report += "• 获取失败\n"

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
