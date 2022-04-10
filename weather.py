#weather.py
import discord

color = 0x6A0DAD
#specified variable names to use, must be exact from API. goes in order of dictionary in API
toDisplay = {
    'temp' : 'Temperature',
    'feels_like' : 'Feels Like',
    'temp_min' : 'Minimum Temperature',
    'temp_max' : 'Maximum Temperature',
    'humidity' : 'Humidity',
    'speed' : 'Wind Speed',
    'clothing_advice' : 'Clothing Advice',
    'weather' : 'Conditions'
}

def selectData(data):
    #modify data here
    if 'pressure' in data:
        del data['pressure']
    if 'deg' in data:
        del data['deg']
    if 'gust' in data:
        del data['gust']
    if 'sea_level' in data:
        del data['sea_level']
    if 'grnd_level' in data:
        del data['grnd_level']
    if 'id' in data:
        del data['id']
    if 'main' in data:
        del data['main']
    if 'icon' in data:
        del data['icon']
    return data

def weather_message(data, city):
    city = city.title()
    message = discord.Embed(
        title = f'{city} Weather',
        description = f'Weather data in {city}.',
        color = color
    )

    clothingAdvice = ''
    high = data['temp_max']
    if high >= 90:
        clothingAdvice = 'Wear as little clothing as possible. Loose & airy clothing advised.'
    elif high >= 80:
        clothingAdvice = 'Light clothing advised. Loose & airy clothing a plus but not necessary.'
    elif high >= 70:
        clothingAdvice = 'Cotton and breathable fabrics advised. Enjoy the nice weather!'
    elif high >= 60:
        clothingAdvice = 'Layers not necessary, but could be chilly. You may want to have a light jacket.'
    elif high >= 50:
        clothingAdvice = 'At least one extra light layer is advised. Pants are optional but recommended.'
    elif high >= 40:
        clothingAdvice = 'Long pants highly advised. Keep a moderate extra layer on.'
    elif high >= 30:
        clothingAdvice = 'Thick winter coat and warm pants advised. Extra insulation recommended.'
    else:
        clothingAdvice = 'Many thick layers and thermals highly recommended!'

    #assign our new clothing advice to a new dictionary key
    data['clothing_advice'] = clothingAdvice

    for key in data:
        #a field has a name and a value
        message.add_field(
            name = toDisplay[key],
            value = str(data[key]),
            inline = False
    )

    return message

def error_message(city):
    city = city.title()
    return discord.Embed(
        title = 'Error',
        description = f'The city {city} does not exist.',
        color = color
    )
