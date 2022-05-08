#This discord bot will use cataas (cats as a service) and discord.py to respond to users with their input placed onto the image of a cat.


"""
to host this bot, create a file in the same file as this one called "config.json"
In the file write:
{
    "TOKEN": "paste your token here"
}

you could also just paste your token in the line at the bottom
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



@client.event #event triggers whenever a message is recieved
async def on_message(message):
    if message.author == client.user:#dont respond to yourself please mr bot
        return
    #make sure that we are actually getting the input and that the format is correct for embeding
    if message.content.startswith("test"):
         await message.channel.send("your message was: " +message.content+ " https://cataas.com/cat/says/we%20are%20so%20close ")
         

    if message.content.startswith("test2"): await message.channel.send("test 2 complete")


    #this is just so that the bot works in some capacity while it is being developed.
    if message.content.startswith("cat"): await message.channel.send("https://cataas.com/cat/says/"+message.content)

    #this is very stupid but with this, if someone just says the word slay then the bot will respond with an image of a cat that just says "slay"
    if message.content.startswith("slay"): await message.channel.send("https://cataas.com/cat/says/"+message.content)
    if message.content.startswith("SLAY"): await message.channel.send("https://cataas.com/cat/says/"+message.content)
    if message.content.startswith("Slay"): await message.channel.send("https://cataas.com/cat/says/"+message.content)



    #silly stuff that achieves nothing
    if message.content.startswith("hello world"): await message.channel.send("https://cataas.com/cat/says/hello%20world")




#take the message that begins with say, replace the spaces between each word with %20 and remove "say" from the string. then output the link

#THE PROBLEM IS NOW SOLVEABLE
#(currently this word will just kill the whole bot)
#TODO: just recreate this in a smaller program from scratch
    if message.content.startswith("say"):
        def addSyntax(phrase):
            words = ""
        for things in words:
            if things in " _":
                words = words + "%20"
        else:
            words = words + things
            return words

        




        print(message.content)
        catStage1 = addSyntax(words)
        catStage2 = catStage1.replace("say","",1)

        print(catStage2)




    #example of how cataas urls work: https://cataas.com/cat/says/hello%20world
    #note the %20 between the words.





#the token is coming from a seperate and very secret file
client.run(token)
