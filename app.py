import random, string, discord, os

def passworsd_generator(length):
    elementos = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    password = ""
    for _ in range(length):
        password += random.choice(elementos)
    return password

def meme():
    with open ("img/img1.jpeg","rb") as f:
        picture = discord.File(f)
    return picture

def memes():
    lista_meme = random.choice(os.listdir("img"))
    with open (f"img/{lista_meme}","rb") as f:
        picture = discord.File(f)
    return picture