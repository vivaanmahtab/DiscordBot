
# author: Vivaan Mahtab
# Created: 6.27.2020
# Most Recent Edit: 6.27.2020

import discord
import os
from discord.ext import commands
from .backend import Backend


class Soundboard(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.players = {}

    # commands
    @commands.command(pass_context=True)
    async def load(self, context, audio):
        voice_client = context.guild.voice_client

        # check if audio clip exists:
        print os.path.isdir()
        if not os.path.isdir(f"./audio_clips/{audio.lower()}"):
            await context.send("audio clip wasn't found :(")
            return

        player = voice_client.create.ffmpeg_player(f"audio_clips/{audio.lower()}.mp3",
                                                   after=lambda: print(f'now playing: {context.content}.mp3'))
        player.start()



def setup(client):
    client.add_cog(Soundboard(client))
