import discord, os
import app
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("dt")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(name="psw")
async def passwords(ctx, largo=25):
    data = app.passworsd_generator(largo)
    await ctx.send(f"🔒 contraseña generada: {data}")

bot.run(token)