import discord 
class eventHandler:
        def __init__(self):
            self.default = true
        def event(self, message):
            if message.author == client.user:
                return
            else:
                if message.content.startswith('!hello'):
                    print(message.author)
                    return "Hello "+ message.author.mention
                if message.content.startswith('!kill'):
                    quit()