# get_user_info.py

import requests
import json

def get_user_info():
    with open("../data/slack_token.txt", "r") as file:
        SLACK_BOT_TOKEN = file.read().strip()

    SLACK_API_URL = "https://slack.com/api/users.list"
    headers = {"Authorization": f"Bearer {SLACK_BOT_TOKEN}"}

    response = requests.get(SLACK_API_URL, headers=headers)
    data = response.json()

    users_filtered = []
    for member in data.get("members", []):
        user_id = member.get("id")
        username = member.get("name")
        profile = member.get("profile", {})
        display_name = profile.get("display_name") or profile.get("real_name")

        users_filtered.append({
            "id": user_id,
            "username": username,
            "name": display_name
        })

    output_file = "../data/slack_users_list.json"
    with open(output_file, "w") as file:
        json.dump(users_filtered, file, separators=(',', ': '))

    return output_file


if __name__ == "__main__":
    file_path = get_user_info()
    print(f"Wrote user info to {file_path}")

