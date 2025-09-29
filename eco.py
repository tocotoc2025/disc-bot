import discord
def etiqueta_reutilizar():
    embed = discord.Embed(
        title = "Ideas de reutilizado de materiales",
        description= "¡Aquí tienes algunas ideas para reutilizar materiales y reducir el desperdicio! ♻️",
        color= 0xB2A4FF
    )
    embed.add_field(
        name ="1. tarros de cristal" ,
        value ="Puedes reutilizar tarros de cristal como recipientes para almacenar alimentos, hacer velas caseras o como macetas para plantas pequeñas.",
        inline =False
    )
    embed.set_thumbnail(url= "https://i.postimg.cc/KztChyMG/pyejemplo.jpg")
    return embed