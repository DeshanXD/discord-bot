import discord
from discord.ext import commands
from settings import TOKEN
from settings import SERVER_ID
 
client = discord.Client()

@client.event
async def on_message(messsage):
    id = client.get_guild(int(SERVER_ID))
    
    # if messsage.content.lower().find("!hello") != -1:
    #     await messsage.channel.send("Hi") 
        
    if messsage.content == "!users":
        await messsage.channel.send(id.member_count)


client.run(TOKEN)