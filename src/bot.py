#!/usr/bin/env python3

import discord
import os
from dotenv import load_dotenv


print("debug")
#exit()

# Load environment variables from .env file
load_dotenv()

# Define the intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent

# Create an instance of a client with intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

# Run the bot with the token
TOKEN = must_get_from_config()
if TOKEN is None:
    raise ValueError("Discord token is not set. Please check your environment variables.")
client.run(TOKEN)
