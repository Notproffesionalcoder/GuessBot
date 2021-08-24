import discord
import aiohttp
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix=".")
TOKEN = os.getenv("TOKEN")
    
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name='.support | By ~Rishi#0100'))
    print(f"Logged in as {client.user.name}")
    print(f"Bot ID: {client.user.id}")
    @client.command()
async def support(ctx):
    await ctx.send("List of commands:  `.gtn`." )
    @client.command()
async def gtn(ctx):
    computer = random.randint(1, 10)
    await ctx.send("Guess my number. It could be any from 1 to 10.")
