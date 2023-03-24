import discord
import requests
import json
import asyncio

intents = discord.Intents.all()
client = discord.Client(intents=intents, privileged=True)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))



def generate_image(prompt):
    url = 'https://api.openai.com/v1/images/generations'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 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'
    }
    data = {
        "model": "image-alpha-001",
        "prompt": prompt,
        "num_images": 1,
        "size": "512x512",
        "response_format": "url"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()['data'][0]['url']

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/generate_image'):
        prompt = message.content[15:]
        image_url = generate_image(prompt)
        await message.channel.send(image_url)

client.run('MTA3MzQ4MDIxMjk4NzI1Mjc2Ng.G_9eJa.0YlukHjEZCbYxnnkNyUhNK5G4wRvJ5G7e2O3-M')