#This discord bot will use cataas (cats as a service) and discord.py to respond to users with their input placed onto the image of a cat.


"""
to host this bot, create a file in the same file as this one called "config.json"
In the file write:
{
    "TOKEN": "paste your token here"
}
"""
import discord
import json

#catsaymessage = (message.content)




#getting the token from the config.json
with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]


client = discord.Client()


#declare victory (for coming online without crashing)
@client.event
async def on_ready():
    print("now online: {0.user}".format(client))

#hi is this working hi daniel

@client.event #event triggers whenever a message is recieved
async def on_message(message):
    if message.author == client.user:
        return
    #make sure that we are actually getting the input and that the format is correct for embeding
    if message.content.startswith("test"):
         await message.channel.send("your message was: " +message.content+ " https://cataas.com/cat/says/we%20are%20so%20close ")
         

    if message.content.startswith("test2"): await message.channel.send("test 2 complete")


    #this is just so that the bot works in some capacity while it is being developed.
    if message.content.startswith("cat"): await message.channel.send("https://cataas.com/cat/says/"+message.content)


    if message.content.startswith("say"): 

        #idk why this wont work but i need to sleep
        
        #await message.channel.send:()
        words = (message.content)
        for things in words:
            if things in " _":
                words = words + "%20"
            else:
                words = words + things
        return words

        catStage1 = add_syntax(words)
        catStage2 = catStage1.replace("say","",1)


        await message.channel.send(catStage2)





    #example of how cataas urls work: https://cataas.com/cat/says/hello%20world    





#the token is coming from a seperate and very secret file
client.run(token)
