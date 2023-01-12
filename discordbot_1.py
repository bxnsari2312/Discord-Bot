import discord
from discord.ext import commands
from discord import FFmpegAudio
import requests
import json

TOKEN = "MTA1OTkxMDA4NzU3NTA4MTAzMA.Gn5Ozu.-uiI6irqMt9ujwqm1fdzMuJFLOtiE43iqvaXbU"
CODE = 1060294247040958558
intents = discord.Intents.default()
intents.members = True


client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print("Bot is ready!")
    print("------------------------------")


@client.command()
async def hi(ctx):
    await ctx.send("Hello I am slothy")


@client.event
async def on_member_join(member):
    jokesurl = "https://joke3.p.rapidapi.com/v1/joke"

    payload = {
        "content": "A joke here",
        "nsfw": "false"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "e3b9c95d07msh12fdf7c21a3d0c6p1b9e61jsn95b8c0ed2b5a",
        "X-RapidAPI-Host": "joke3.p.rapidapi.com"
    }
    response = requests.request(
        "POST", jokesurl, json=payload, headers=headers)
    print(response.text)
    channel = client.get_channel(CODE)
    await channel.send("Hello")
    await channel.send(json.loads(response.text)['content'])


@client.event
async def on_member_remove(member):
    channel = client.get_channel(CODE)
    await channel.send("Goodbye")


@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegAudio('audio.mp3')
        player = voice.play(source)

    else:
        await ctx.send("You are not in a voice channel, need to be in a voice channel to run the command!")


@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guide.voice_client.disconnect()
        await ctx.send("I left the voice channel")
    else:
        await ctx.send("I am not in the voice channel")


client.run(TOKEN)
