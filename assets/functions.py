import discord
import requests
import json
import asyncio

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