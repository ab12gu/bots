import os
import json
import discord
from discord.ext import commands
import asyncio

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SUB_FILE = os.path.join(SCRIPT_DIR, "subscribers.json")

# Load subscribers from JSON
if os.path.exists(SUB_FILE):
    with open(SUB_FILE) as f:
        subscribers = json.load(f)
else:
    subscribers = []

MESSAGE_TO_SEND = "Hello! This is a DM from the bot."

## OVERRIDE LOOP WITH SELF ID
TARGET_USER_ID = int(os.getenv("TARGET_USER_ID"))

intents = discord.Intents.default()
intents.members = True  # Required to fetch users
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():

    print(f"Logged in as {bot.user}")

    for user_id in subscribers:
        try:
            user = await bot.fetch_user(int(user_id))

            ## OVERRIDE
            user = await bot.fetch_user(TARGET_USER_ID)
            if user:
                await user.send(MESSAGE_TO_SEND)
                print(f"✅ Sent DM to {user.name}")
        except Exception as e:
            print(f"❌ Could not DM {user_id}: {e}")

        # Add delay to avoid rate limits
        await asyncio.sleep(1)

    # Close after sending all DMs
    await bot.close()

if __name__ == "__main__":
    bot.run(os.getenv("BOT_TOKEN"))
