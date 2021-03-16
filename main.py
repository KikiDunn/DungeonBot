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
dog = bot.dog()
dog.print()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        if message.content.startswith('!hello'):
            await message.channel.send("Hello "+ message.author.mention)
        if message.content.startswith('!kill'):
            quit()
with open('key') as fp:
    token = fp.readline().strip()
    client.run(token)
