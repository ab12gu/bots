import os
from slack_sdk import WebClient

# Read token from file
with open("slack_token.txt", "r") as f:
    SLACK_BOT_TOKEN = f.read().strip()

client = WebClient(token=SLACK_BOT_TOKEN)
#client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

response = client.users_list()

with open("206bikepolo_users.txt", "w") as f:
    for user in response['members']:
        # Skip bots and deactivated users
        if not user.get("deleted") or user.get("is_bot"):
            user_id = user["id"]
            username = user["name"]
            real_name = user.get("real_name", "(no real name)")
            display_name = user["profile"].get("display_name", "(no display name)")
            print(user_id, username, real_name, display_name)


        f.write(f"{user_id} {username} {real_name} {display_name}\n")

print("User list exported to 206bikepolo_users.txt")
