import discord
from discord.ext import commands

# Set up the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Event to set the bot's status
@bot.event
async def on_ready():
    # Custom status
    activity = discord.Game(name="Building Bots at Bot Factory!")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'Logged in as {bot.user}')

# Your bot's token
bot.run('YOUR_BOT_TOKEN')
