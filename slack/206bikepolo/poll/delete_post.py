# Delete messsage posted by slackbot
# - need to run following code on local bash
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

POLL_BOT_TOKEN = os.getenv("POLL_BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
MESSAGE_TS = os.getenv("MESSAGE_TS")

res = requests.post("https://slack.com/api/chat.delete", json={
    "channel": CHANNEL_ID,
    "ts": MESSAGE_TS
}, headers={
    "Authorization": f"Bearer {POLL_BOT_TOKEN}",
    "Content-Type": "application/json"
})

print(res.json())
