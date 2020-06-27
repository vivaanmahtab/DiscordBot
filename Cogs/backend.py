
# author: Vivaan Mahtab
# Created: 6.20.2020
# Most Recent Edit: 6.20.2020

import discord
from discord.ext import commands


class Backend(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events

    # Commands
    @commands.command(pass_context=True)
    async def join(self, context):
        try:
            channel = context.message.author.voice.channel
            await channel.connect()
            return True
        except AttributeError:
            await context.channel.send("You have to be in a voice channel!\n-management")
            return False
        except:
            await context.channel.send("Failed to connect,\nreport to management")
            return None

    @commands.command(pass_context=True)
    async def leave(self, context):
        server = context.message.guild.voice_client
        await server.disconnect()



def setup(client):
    client.add_cog(Backend(client))
