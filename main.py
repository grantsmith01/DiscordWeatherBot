#main.py
import os
import discord
import requests
import json
from weather import *

#open token. not advised for anyone looking at this code, always hide your tokens. for demonstration purposes only
TOKEN = 'OTYyNDQ3Mjk2ODk1Nz.gyOTUz.YlHq5A.WKSXqgvD8EleBWWjwTwsiuJsLjw'
commandPrefix = 'weather.'
api_key = 'f340f2c8385af9d298d7e473ad48d43f'
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{commandPrefix}[city]'))

@client.event
async def on_message(message):
    #if the message is not being sent by the bot, and the content starts with 'weather.', ...
    if message.author != client.user and message.content.startswith(commandPrefix):
        #remove the prefix to extract the actual command
        city = message.content.replace(commandPrefix, '').lower()
        #if the command itself is greater than 0 characters...
        if len(city) >= 1:
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial'
            try:
                #combining the 2 dictionaries that the API provides
                features = { **json.loads(requests.get(url).content)['main'],
                             **json.loads(requests.get(url).content)['wind'] }
                data = selectData(features)
                await message.channel.send(embed = weather_message(data, city))
            except KeyError:
                await message.channel.send(embed = error_message(city))

client.run(TOKEN)
