import os
import requests

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

text = (
    "Great Games Today!"
)
res = requests.post("https://slack.com/api/chat.postMessage", json={
    "channel": CHANNEL_ID,
    "text": text
}, headers={
    "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
    "Content-Type": "application/json"
})

print("Posted:", res.json())
