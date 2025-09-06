import random, string
def passworsd_generator(length):
    elementos = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    password = ""
    for _ in range(length):
        password += random.choice(elementos)
    return password