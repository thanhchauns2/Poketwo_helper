import discord
import playsound

ID = 934376539783573565

client = discord.Client()

@client.event
async def on_ready():
    print("Main user logged in: {0.user}".format(client))

@client.event
async def on_message(message):
    channel = client.get_channel(ID)
    if message.content == "!gotem" and message.channel.id == ID:
        playsound.playsound('C:/Users/Laptop88_LTV/Documents/GitHub/Python/Sound notification/hare hare ya.mp3')

client.run("OTM1NzQwNzQyNDkwNTU0NDE5.YfDCqw.vOcTzMlCVtCMCWE5n7jvm5p8DF0", bot=False)