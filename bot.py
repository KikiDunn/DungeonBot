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
                    print (message.author.id)
                    if .format(message.author.id) == "719874724951359578":
                        return "Process terminated."
                return ""