
# author: Vivaan Mahtab
# Created: 6.20.2020
# Most Recent Edit: 6.20.2020

import os
import discord
from discord.ext import commands, tasks

client = commands.Bot(command_prefix='>')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("games on his phone"))
    print("loaded")


# @client.command()
# async def load(context, extension):
#     client.load_extension(f"cogs.{extension}")


# @client.command()
# async def unload(context, extension):
#     client.unload_extension(f"cogs.{extension}")


client.run("NzI0MDYyMTA0NTM3MTM3MTYy.Xu665Q.kLOR5yIsc_QtSla-oO9gR3OoIZE")
