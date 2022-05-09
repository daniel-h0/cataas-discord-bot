#This discord bot will use cataas (cats as a service) and discord.py to respond to users with their input placed onto the image of a cat.


"""
to host this bot, create a file in the same file as this one called "config.json"
In the file write:
{
    "TOKEN": "paste your token here"
}

you could also just paste your token in the line at the bottom
client.run(right here)
"""

import discord
import json

#getting the token from the config.json
with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]


client = discord.Client()

#declare victory (for coming online without crashing)
@client.event
async def on_ready():
    print("now online: {0.user}".format(client))



@client.event #event triggers whenever a message is received
async def on_message(message):
    if message.author == client.user:#this is to stop the bot from responding to itself
        return

#take the message that begins with say, replace the spaces between each word with %20 and remove "say" from the string. then output the link

    if message.content.startswith("say"):
        #print each usage of the bot to the terminal
        print("catsay triggered:", message.content)
        catMessage = message.content
        #cut the command out of the variable
        catCutOff = catMessage[4:]
        #replace the spaces with %20 (for the link to work)
        catSyntaxed = catCutOff.replace(" ", "%20")
        #output the link + the final result
        await message.channel.send("https://cataas.com/cat/says/"+catSyntaxed)


    #example of how cataas urls work: https://cataas.com/cat/says/hello%20world
    #note the %20 between the words.


#the token is coming from the config.json file
client.run(token)
