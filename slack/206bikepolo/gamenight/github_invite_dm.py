import os
import json
import textwrap
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

#SLACK_BOT_TOKEN = ""
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

# Read token from file
#with open("slack_token.txt", "r") as f:
    #SLACK_BOT_TOKEN = f.read().strip()

client = WebClient(token=SLACK_BOT_TOKEN)

## Replace with the user ID you want to DM
#USER_ID = "U06AWV00DL2"

# Load user list from JSON
with open("gamenight/subscribers.json", "r") as f:
    users = json.load(f)

for user in users:
    user_id = user["id"] #USER_ID

    message = textwrap.dedent(f"""
        Eyyo {user.get('username', '')}!

        Gamenight tomorrow @ 6pm (Sat, 9-20)
        In Interbay, near Queen Anne

        Check website for deets:
        <https://byobg.com|byobg.com>
    """)

    try:
        # Open DM channel
        dm = client.conversations_open(users=USER_ID)
        channel_id = dm["channel"]["id"]

        # Send message
        client.chat_postMessage(channel=channel_id, text=message)

        print(f"Message sent to {USER_ID}")

    except SlackApiError as e:
        print(f"Error sending DM: {e.response['error']}")
