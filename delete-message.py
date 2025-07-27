import requests
import os

SLACK_TOKEN = os.getenv("SLACK_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
MESSAGE_TS = os.getenv("MESSAGE_TS")

res = requests.post("https://slack.com/api/chat.delete", json={
    "channel": CHANNEL_ID,
    "ts": MESSAGE_TS
}, headers={
    "Authorization": f"Bearer {SLACK_TOKEN}",
    "Content-Type": "application/json"
})

print(res.json())