import os
import requests

SLACK_TOKEN = os.getenv("SLACK_WEBSITE_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

text = "*Wednesday newbie polo 6pm till dark @ Judkin's Park*\nReact with 🚴 if you're in!"

res = requests.post("https://slack.com/api/chat.postMessage", json={
    "channel": CHANNEL_ID,
    "text": text
}, headers={
    "Authorization": f"Bearer {SLACK_TOKEN}",
    "Content-Type": "application/json"
})

print("Posted:", res.json())
