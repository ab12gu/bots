import discord
from discord.ext import commands
import json
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
SUB_FILE = "subscribers.json"

# Load subscribers
if os.path.exists(SUB_FILE):
    with open(SUB_FILE) as f:
        subscribers = set(json.load(f))
else:
    subscribers = set()

intents = discord.Intents.default()
intents.message_content = True  # <-- required to read messages
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def subscribe(ctx):
    subscribers.add(ctx.author.id)
    with open(SUB_FILE, "w") as f:
        json.dump(list(subscribers), f)
    await ctx.send("You have subscribed!")

@bot.command()
async def unsubscribe(ctx):
    subscribers.discard(ctx.author.id)
    with open(SUB_FILE, "w") as f:
        json.dump(list(subscribers), f)
    await ctx.send("You have unsubscribed!")

bot.run(BOT_TOKEN)

if __name__ == "__main__":
    # only runs when the file is executed directly
    main()
