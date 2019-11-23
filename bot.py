import discord
from discord.ext import commands
from settings import TOKEN
from settings import SERVER_ID
 
client = discord.Client()

@client.event
async def on_message(messsage):
    id = client.get_guild(int(SERVER_ID))
    channels = ["commands"]
    
    if str(messsage.channel) in channels:
        if messsage.content.lower().find("!hello") != -1:
            await messsage.channel.send("Hi") 
            
        elif messsage.content == "!users":
            await messsage.channel.send(id.member_count)

@client.event
async def on_member_join(message):
    # id = client.get_guild(int(SERVER_ID))
    # channels = ["commands"]
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""Welcome to the server {member.mention}""")



client.run(TOKEN)