#to run:
#cd DungeonBot/
#setsid python3 main.py
#to kill 
#ps -ef
#kill ####
import discord 
import os
import bot

client  = discord.Client()
_bot = bot.eventHandler()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    output = _bot.event(message, client)
    if (output != ""):
        await message.channel.send(output)
with open('key') as fp:
    token = fp.readline().strip()
    client.run(token)
