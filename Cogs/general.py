
# author: Vivaan Mahtab
# Created: 6.20.2020
# Most Recent Edit: 6.27.2020

import discord
from discord.ext import commands


class General(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "die":
            await message.channel.send("in game")
            await commands.Bot.process_commands(self=self.client, message=message)

    # Commands
    @commands.command(aliases=["purge"])
    async def clear(self, context, amount=0):
        amount += 1
        await context.channel.purge(limit=amount)


    @commands.command()
    async def ping(self, context):
        await context.send(f"Pong! The response time is: `{round(self.client.latency * 1000)}ms`!")

    @commands.command()
    async def dynobot(self, context):
        await context.send(f"searching...\nError 404: Not found (but always still here in our hearts)")


def setup(client):
    client.add_cog(General(client))
