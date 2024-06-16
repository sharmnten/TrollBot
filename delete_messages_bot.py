import os
import discord
from discord.ext import commands

# Replace 'username_to_delete' with the username you want to target
USERNAME_TO_DELETE = 'inorivoid'

# Get the bot token from the environment variable
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Set up the bot with the appropriate intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')
    print('------')

@bot.event
async def on_message(message):
    if message.author.name == USERNAME_TO_DELETE:
        try:
            await message.delete()
            print(f'Deleted message from {USERNAME_TO_DELETE}')
        except discord.Forbidden:
            print(f'Cannot delete message from {USERNAME_TO_DELETE}, insufficient permissions.')
        except discord.HTTPException as e:
            print(f'Failed to delete message from {USERNAME_TO_DELETE}: {e}')

bot.run(TOKEN)
