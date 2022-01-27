import discord
import playsound

ID = # channel ID

client = discord.Client()

@client.event
async def on_ready():
    print("Main user logged in: {0.user}".format(client))

@client.event
async def on_message(message):
    channel = client.get_channel(ID)
    if message.content == "!gotem" and message.channel.id == ID:
        playsound.playsound(sound directory)

client.run(token, bot=False)
