import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # needed for DMs

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def dm(ctx, member: discord.Member, *, message):
    try:
        await member.send(message)
        await ctx.send(f"✅ Sent DM to {member.display_name}")
    except:
        await ctx.send(f"❌ Could not DM {member.display_name}")

bot.run("BYOBG_BOT_TOKEN")

