import discord
from discord.ext import commands
import json
import os
import subprocess

# Environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
REPO_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(SCRIPT_DIR)
SUB_FILE = os.path.join(PARENT_DIR, "data", "subscribers_new.json")

# Load subscribers
if os.path.exists(SUB_FILE):
    with open(SUB_FILE) as f:
        subscribers = json.load(f)
else:
    subscribers = []

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


def push_json_to_github():
    """Commit and push the updated subscribers.json to GitHub."""
    try:
        os.chdir(REPO_PATH)

        # Configure Git identity
        subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
        subprocess.run(
            ["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"],
            check=True,
        )

        # Stage changes
        subprocess.run(["git", "add", SUB_FILE], check=True)

        # Commit (ignore failure if no changes)
        subprocess.run(
            ["git", "commit", "-m", "Update subscribers.json [skip ci]"],
            check=False,
        )

        # Push using the origin remote (checkout already configured credentials)
        subprocess.run(["git", "push", "origin", "main"], check=True)

        print("SUCCESSFULLY Pushed subscribers.json to GitHub")
    except subprocess.CalledProcessError as e:
        print("ERROR Git push failed:", e)


@bot.command()
async def subscribe(ctx):

    new_entry = {
            "id": ctx.author.id, 
            "name": ctx.author.name, 
            "display_name": ctx.author.display_name, 
            "global_name": ctx.author.global_name
    }
    subscribers.append(new_entry)
    with open(SUB_FILE, "w") as f:
        json.dump(subscribers, f, indent=2)
    await ctx.send("You have subscribed!")
    push_json_to_github()


@bot.command()
async def unsubscribe(ctx):
    subscribers = [s for s in subscribers if s["id"] != ctx.author.id]
    with open(SUB_FILE, "w") as f:
        json.dump(subscribers, f, indent=2)
    await ctx.send("You have unsubscribed!")
    push_json_to_github()


bot.run(BOT_TOKEN)

