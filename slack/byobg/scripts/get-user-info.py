import json
from slack_sdk import WebClient


def get_user_info():
    # Read token from file
    with open("../data/slack_token.txt", "r") as f:
        SLACK_BOT_TOKEN = f.read().strip()

    client = WebClient(token=SLACK_BOT_TOKEN)
    # import os
    # client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

    response = client.users_list()

    users_filtered = []
    output_txt_file = "../data/206bikepolo_users.txt"
    output_json_file = "../data/206bikepolo_users.json"

    with open(output_txt_file, "w") as f:
        for user in response["members"]:
            # Skip bots and deactivated users
            if not user.get("deleted") or user.get("is_bot"):
                user_id = user["id"]
                username = user["name"]
                real_name = user.get("real_name", "(no real name)")
                display_name = user["profile"].get("display_name", "(no display name)")
                print(user_id, username, real_name, display_name)

            f.write(f"{user_id} {username} {real_name} {display_name}\n")

            users_filtered.append(
                {
                    "id": user_id,
                    "name": username,
                    "real_name": real_name,
                    "display_name": display_name,
                }
            )

    with open(output_json_file, "w") as f:
        json.dump(users_filtered, f, indent=4)


if __name__ == "__main__":
    file_path = get_user_info()
    print("User list exported to 206bikepolo_users.txt and 206bikepolo_users.json")
