import discord
from discord.ext import commands
import json
import os
import subprocess

# Environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
REPO_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SUB_FILE = os.path.join(SCRIPT_DIR, "subscribers.json")

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
    subscribers.add(ctx.author.id)
    with open(SUB_FILE, "w") as f:
        json.dump(list(subscribers), f, indent=2)
    await ctx.send("You have subscribed!")
    await ctx.send(ctx.author.id)
    await ctx.send(ctx.author.name)
    await ctx.send(ctx.author.display_name)
    await ctx.send(ctx.author.global_name)
    push_json_to_github()


@bot.command()
async def unsubscribe(ctx):
    subscribers.discard(ctx.author.id)
    with open(SUB_FILE, "w") as f:
        json.dump(list(subscribers), f, indent=2)
    await ctx.send("You have unsubscribed!")
    push_json_to_github()


bot.run(BOT_TOKEN)

