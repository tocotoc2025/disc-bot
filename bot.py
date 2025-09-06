import discord, os
from dotenv import load_dotenv

import app

load_dotenv()
token = os.getenv("dt")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Hola, hemos iniciado sesión como {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('?hola'):
       await message.channel.send('Hola bienvenido a mi primer bot') 
    elif message.content.startswith('?contraseña'):
        x= app.passworsd_generator(25)
        await message.channel.send(f'Tu contraseña es: {x}')

client.run(token)