#import discord 
#import os

#client  = discord.Client()
#@client.event
#async def on_ready():
#    print('We have logged in as {0.user}'.format(client))

#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#
#    if message.content.startswith('!hello'):
#        await message.channel.send('Hello!')
#with open('key') as fp:
#    client.run(os.getenv(fp.readline().strip()))
with open('key') as fp:
    print(fp.readline().strip())