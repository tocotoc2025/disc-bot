import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

# Cargar token
load_dotenv()
TOKEN = os.getenv("dt")

if not TOKEN:
    raise ValueError("No se encontró el token en el archivo .env")

# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="$",
    intents=intents
)

# Datos
CALENTAMIENTO = [
    "🌡️ El calentamiento global aumenta la temperatura del planeta.",
    "🏭 Los gases contaminantes contribuyen al calentamiento global.",
    "🧊 El deshielo de los glaciares es una de sus consecuencias.",
    "🌳 Plantar árboles ayuda a combatir el calentamiento global.",
    "⚡ Ahorrar energía reduce las emisiones contaminantes."
]

RECICLAJE = [
    "♻️ Separa plástico, papel y vidrio para reciclar correctamente.",
    "📦 Reutiliza cajas de cartón antes de desecharlas.",
    "🛍️ Usa bolsas reutilizables cuando hagas compras.",
    "📚 Dona libros que ya no utilices.",
    "🥤 Lava los envases antes de reciclarlos."
]

DATOS_ECO = [
    "🌳 Un árbol puede absorber grandes cantidades de CO₂ durante su vida.",
    "💧 Cerrar el grifo mientras te cepillas los dientes ahorra agua.",
    "♻️ Reciclar una lata ahorra energía comparado con fabricar una nueva.",
    "🌎 Más del 70% de la superficie terrestre está cubierta por agua.",
    "🔋 Las pilas deben reciclarse en puntos especiales."
]

RETOS_ECO = [
    "🚶 Camina o usa bicicleta hoy si puedes.",
    "💡 Apaga las luces que no estés utilizando.",
    "🥤 Evita usar plásticos de un solo uso durante el día.",
    "🌱 Planta una semilla o cuida una planta.",
    "🚿 Intenta tomar una ducha más corta hoy."
]

REUTILIZAR = {
    "botella": "🌱 Convierte la botella en una maceta para una planta.",
    "caja": "📦 Utilízala para guardar útiles escolares.",
    "lata": "✏️ Conviértela en un portalápices.",
    "frasco": "🖍️ Úsalo para guardar lápices, colores o clips.",
    "papel": "✂️ Haz manualidades u origami.",
    "ropa": "🧹 Conviértela en un paño de limpieza.",
    "cuaderno": "📓 Usa las hojas que aún estén en blanco.",
    "calcetin": "🐻 Crea una marioneta decorándolo.",
    "revista": "🎨 Haz collages con las imágenes.",
    "carton": "🏠 Construye una maqueta sencilla.",
    "tubo": "🚀 Úsalo como portalápices."
}

# Eventos
@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

# Comandos
@bot.command()
async def hello(ctx):
    await ctx.send(
        "🌍 **Bot Ecológico** 🌱\n\n"
        "**Comandos disponibles:**\n"
        "`$calentamiento`\n"
        "`$reciclar`\n"
        "`$datoeco`\n"
        "`$retoeco`\n"
        "`$reutilizar objeto`\n\n"
        "**Ejemplo:**\n"
        "`$reutilizar botella`"
    )

@bot.command()
async def calentamiento(ctx):
    await ctx.send(random.choice(CALENTAMIENTO))

@bot.command()
async def reciclar(ctx):
    await ctx.send(random.choice(RECICLAJE))

@bot.command()
async def datoeco(ctx):
    await ctx.send(random.choice(DATOS_ECO))

@bot.command()
async def retoeco(ctx):
    await ctx.send(random.choice(RETOS_ECO))

@bot.command()
async def reutilizar(ctx, *, objeto):
    objeto = objeto.lower()

    for nombre, idea in REUTILIZAR.items():
        if nombre in objeto:
            await ctx.send(idea)
            return

    await ctx.send(
        f"🌿 No conozco una forma específica de reutilizar '{objeto}', "
        "pero podrías convertirlo en una decoración, organizador o manualidad."
    )

# Ejecutar bot
bot.run(TOKEN)