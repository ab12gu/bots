import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Needed to fetch members

bot = commands.Bot(command_prefix="!", intents=intents)

# Replace with the target user's Discord ID
TARGET_USER_ID = int(os.getenv("TARGET_USER_ID")) # <-- put their ID here
MESSAGE_TO_SEND = "Hello! This is a DM from the bot."

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    user = await bot.fetch_user(TARGET_USER_ID)
    if user:
        try:
            await user.send(MESSAGE_TO_SEND)
            print(f"✅ Sent DM to {user.name}")
        except Exception as e:
            print(f"❌ Could not DM {user.name}: {e}")
    await bot.close()  # Optional: stops the bot after sending




bot.run(os.getenv("BOT_TOKEN"))

if __name__ == "__main__":
    # only runs when the file is executed directly
    main()
