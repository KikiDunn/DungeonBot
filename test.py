import discord 
import os

client  = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send("Hello "+ message.author.mention)
with open('key') as fp:
    token = fp.readline().strip()
    client.run(token)
#to run:
#cd DungeonBot/
#setsid python3 test.py
#to kill 
#ps -ef
#kill ####