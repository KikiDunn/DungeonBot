import discord 
class eventHandler:
        def __init__(self):
            
        def event(self, message):
            if message.author == client.user:
                return
            else:
                if message.content.startswith('!hello'):
                    await message.channel.send("Hello "+ message.author.mention)
                if message.content.startswith('!kill'):
                    quit()