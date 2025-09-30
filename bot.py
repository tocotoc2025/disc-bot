import discord, os
import app
import eco
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

@bot.command(name="suma")
async def sumar(ctx, *args):
    total = sum(int(x) for x in args)
    await ctx.send(f'El total es: {total}')
    
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(name="psw")
async def passwords(ctx, largo=25):
    data = app.passworsd_generator(largo)
    await ctx.send(f"🔒 contraseña generada: {data}")

@bot.command(name="description")
async def descri(ctx):
    await ctx.send(f"Soy un bot el cual puede reir, mandar memes, ecotips y contraseñas")

@bot.command(name="meme")
async def meme(ctx):
    picture = app.meme()
    await ctx.send(file=picture)

@bot.command(name="memes")
async def memes(ctx):
    picture = app.memes()
    await ctx.send(file=picture)

@bot.command(name = "ecotips")
async def ecotips(ctx):
    tips = eco.etiqueta_reutilizar()
    await ctx.send(embed=tips)

bot.run(token)