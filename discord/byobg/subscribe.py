import discord
from discord.ext import commands
import json
import os
import subprocess

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Adjust this to point to the repo root
REPO_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
SUB_FILE = os.path.join(REPO_PATH, "subscribers.json")


# Load subscribers
if os.path.exists(SUB_FILE):
    with open(SUB_FILE) as f:
        subscribers = set(json.load(f))
else:
    subscribers = set()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

def push_json_to_github():
    """Commit and push the updated subscribers.json to GitHub."""
    try:
        os.chdir(REPO_PATH)  # repo root

        # Reset any unstaged changes (so pull won't fail)
        subprocess.run(["git", "reset", "--hard"], check=True)
        
        # Pull latest changes from main
        subprocess.run(["git", "pull", "origin", "main"], check=True)

        # Add and commit subscribers.json
        subprocess.run(["git", "add", SUB_FILE], check=True)
        subprocess.run(
            ["git", "commit", "-m", "Update subscribers.json [skip ci]"], check=False
        )

        # Push changes
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("✅ Pushed subscribers.json to GitHub")
    except subprocess.CalledProcessError as e:
        print("❌ Git push failed:", e)



@bot.command()
async def subscribe(ctx):
    subscribers.add(ctx.author.id)
    with open(SUB_FILE, "w") as f:
        json.dump(list(subscribers), f)
    await ctx.send("You have subscribed!")
    push_json_to_github()  # push after update

@bot.command()
async def unsubscribe(ctx):
    subscribers.discard(ctx.author.id)
    with open(SUB_FILE, "w") as f:
        json.dump(list(subscribers), f)
    await ctx.send("You have unsubscribed!")
    push_json_to_github()  # push after update

if __name__ == "__main__":
    bot.run(BOT_TOKEN)

