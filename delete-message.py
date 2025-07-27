# Delete messsage posted by slackbot
#
# $ python3 -m venv venv   
# $ source venv/bin/activate  
# $ pip install requests
# $ SLACK_TOKEN='xoxb-..."
# $ CHANNEL_ID='CKHJURLQJ'   
# $ MESSAGE_TS='1753651851.426429'
# $ python3 delete-message.py  
# $ deactivate
#

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
