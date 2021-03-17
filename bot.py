import discord 
class eventHandler:
        def __init__(self):
            self.default = True
        def event(self, message, client):
            if message.author == client.user:
                return ""
            else:
                if message.content.startswith('!hello'):
                    return "Hello "+ message.author.mention
                if message.content.startswith('!kill'):
                    if message.author.name == "KikiJiki":
                        quit()
                return ""