import discord
import json
import os

data = {}
with open("cred.json") as f:
	data = json.load(f)

client_id = data["client_id"]
public_key = data["public_key"]
token = data["token"]
client_secret = data["client_secret"]

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$sup'):
    	await message.channel.send('updog')
	

client.run(token)
print('done')
