
"""
to host this bot, paste your token in the config.json file
This discord bot uses cataas (cats as a service) and discord.py to respond to users with their input placed onto the image of a cat.

"""
import discord
import json

#getting the token and game status from the config.json
with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]
    gamePlayingStatus = data["GAME"]

client = discord.Client()

@client.event #event triggers when the bot comes online
async def on_ready():
    #declare victory (for coming online)
    print("now online: {0.user}".format(client))
    #set the playing status
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(gamePlayingStatus))
    print("Playing status:", gamePlayingStatus)

@client.event #event triggers whenever a message is received
async def on_message(message):
    if message.author == client.user:#this is to stop the bot from responding to itself
        return

#take the message that begins with say, replace the spaces between each word with %20 and remove "say" from the string. then output the link
    if message.content.startswith("say"):
        if message.content == "say":#making sure it does not send an invalid link if someone just says the word say
            await message.channel.send("say what?")
            return
        #print each usage of the bot to the terminal
        print("catsay triggered:", message.content)
        catMessage = message.content
        #cut the command out of the variable
        catCutOff = catMessage[4:]
        #replace the spaces with %20 (for the link to work)
        catSyntaxed = catCutOff.replace(" ", "%20")
        #output the link + the final result
        await message.channel.send("https://cataas.com/cat/says/"+catSyntaxed)
        return

    #example of how cataas urls work: https://cataas.com/cat/says/hello%20world
    #note the %20 between the words.

#the token is coming from the config.json file
client.run(token)
