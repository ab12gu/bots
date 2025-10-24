import os
import json
import textwrap
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

#SLACK_BOT_TOKEN = ""
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

# Read token from file
#with open("slack_token.txt", "r") as f:
    #SLACK_BOT_TOKEN = f.read().strip()

client = WebClient(token=SLACK_BOT_TOKEN)

## Replace with the user ID you want to DM
#USER_ID = "U06AWV00DL2"

# Load user list from JSON
with open("data/subscribers.json", "r") as f:
    users = json.load(f)

for user in users:
    user_id = user["id"] #USER_ID

   
    # Check each user individually
    #info = client.users_info(user="U06AWV00DL2")
    #print("U06AWV00DL2", info["user"]["deleted"], info["user"]["is_bot"])


    # Load message from file
    with open("data/message.txt", "r") as f:
        message = f.read().strip()

    try:
        # Create a private group chat
        channel_name = f"byobg-{user['name']}"  # Using user's name from JSON for channel name
        response = client.conversations_create(
            name=channel_name,
            is_private=True
        )
        channel_id = response["channel"]["id"]

        # Invite both the user and abgup to the channel
        client.conversations_invite(
            channel=channel_id,
            users=f"{user_id},{"U06AWV00DL2"}"  # Replace with abgup's user ID
        )

        # Send message
        client.chat_postMessage(channel=channel_id, text=message)

        print(f"Group chat created and message sent with {user_id} and abgup")

    except SlackApiError as e:
        print(f"Error creating group chat: {e.response['error']}")
