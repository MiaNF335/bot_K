import random

def gen_pass(pass_length):
    caracteres = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''

    for i in range(pass_length):
        c = random.choice(caracteres)
        password += c    
    return password
    
def tirar_moneda():
    result = random.choice(['cara','cruz'])
    return result
    
def emoji_aleatorio():
    lista_emojis = ['🙂', '😎', '🐱', '🌟', '🔥', '🍀', '🎲', '🪙']
    return random.choice(lista_emojis)
