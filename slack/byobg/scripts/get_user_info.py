# get_user_info.py
#
# Terminal Script:
#   $ curl -X GET "https://slack.com/api/users.list" \
#   $   -H "Authorization: Bearer xoxb-<>"

import requests
import os

def get_user_info():


    with open("../data/slack_token.txt", "r") as file:
        SLACK_BOT_TOKEN = file.read().strip()


    SLACK_API_URL = "https://slack.com/api/users.list"

    headers = {"Authorization": f"Bearer {SLACK_BOT_TOKEN}"}       
    response = requests.get(SLACK_API_URL, headers=headers)
    user_data = response.json()

    with open("../data/slack_user_list.txt", "w") as file:
        file.write(str(user_data))
    return user_data


if __name__ == "__main__":
    get_user_info()


