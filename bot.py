import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

TOKEN = os.getenv("dt")

# Verificar que exista el token
if TOKEN is None:
    raise ValueError("No se encontró el token. Revisa tu archivo .env")

# Configurar intents
intents = discord.Intents.default()
intents.message_content = True

# Crear bot
bot = commands.Bot(
    command_prefix="$",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")


# Comando de ayuda
@bot.command()
async def hello(ctx):
    mensaje = (
        "🌍 **Bot Ecológico** 🌱\n\n"
        "**Comandos disponibles:**\n"
        "`$calentamiento`\n"
        "`$reciclar`\n"
        "`$reutilizar objeto`\n\n"
        "**Ejemplos:**\n"
        "`$reutilizar botella`\n"
        "`$reutilizar caja`\n"
        "`$reutilizar lata`"
    )

    await ctx.send(mensaje)


# Información sobre calentamiento global
@bot.command()
async def calentamiento(ctx):
    datos = [
        "🌡️ El calentamiento global es el aumento gradual de la temperatura de la Tierra.",
        "🏭 Los gases producidos por fábricas y vehículos contribuyen al calentamiento global.",
        "🧊 El deshielo de glaciares es una consecuencia del calentamiento global.",
        "🌳 Plantar árboles ayuda a reducir el dióxido de carbono en la atmósfera.",
        "⚡ Ahorrar electricidad ayuda a disminuir las emisiones contaminantes."
    ]

    await ctx.send(random.choice(datos))


# Ideas de reciclaje
@bot.command()
async def reciclar(ctx):
    ideas = [
        "♻️ Separa plástico, papel y vidrio para facilitar el reciclaje.",
        "📦 Reutiliza cajas de cartón antes de desecharlas.",
        "🛍️ Usa bolsas reutilizables cuando vayas de compras.",
        "📝 Aprovecha hojas usadas por una sola cara para tomar apuntes.",
        "🌱 Haz compost con restos de frutas y verduras.",
        "🥤 Lava las botellas antes de llevarlas a reciclar.",
        "📚 Dona libros que ya no utilices."
    ]

    await ctx.send(random.choice(ideas))


# Reutilización
@bot.command()
async def reutilizar(ctx, *, objeto):
    objeto = objeto.lower()

    ideas = {
        "botella": "🌱 Puedes convertirla en una maceta pequeña para una planta.",
        "botella de plastico": "💧 Puedes usarla como regadera con ayuda de un adulto.",
        "caja": "📦 Puedes decorarla y usarla para guardar útiles escolares.",
        "caja de carton": "🎨 Puedes transformarla en un organizador de escritorio.",
        "lata": "✏️ Después de limpiarla bien, puedes usarla como portalápices.",
        "frasco": "🖍️ Puede servir para guardar lápices, colores o clips.",
        "papel": "✂️ Puedes usarlo para hacer origami o manualidades.",
        "cuaderno": "📓 Aprovecha las hojas en blanco para notas o dibujos.",
        "ropa": "🧹 Puede convertirse en un paño para limpiar.",
        "calcetin": "🐻 Puedes hacer una pequeña marioneta decorándola.",
        "revista": "🎨 Puedes recortar imágenes para hacer collages.",
        "carton": "🏠 Puedes construir una maqueta sencilla.",
        "tubo": "🚀 Los tubos de cartón pueden convertirse en portalápices."
    }

    respuesta = None

    for palabra, idea in ideas.items():
        if palabra in objeto:
            respuesta = idea
            break

    if respuesta is None:
        respuesta = (
            f"🌿 No tengo una idea específica para '{objeto}', "
            "pero podrías convertirlo en una manualidad, decoración u organizador."
        )

    await ctx.send(
        f"**Objeto:** {objeto.capitalize()}\n{respuesta}"
    )


# Iniciar el bot
bot.run(TOKEN)