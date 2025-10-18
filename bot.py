import discord
from bot_logic import gen_pass, tirar_moneda, emoji_aleatorio

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('holaaa'):
        await message.channel.send("H!")
    elif message.content.startswith('chauuu'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('como estas?'):
        await message.channel.send("Bien y tu?")
    elif message.content.startswith('moneda'):
        await message.channel.send('la moneda giro y salio:' + tirar_moneda)
    elif message.content.startswith('emoji'):
        await message,channel.send('el emoji que te toco fue:' + emoji_aleatorio)
    else:
        await message.channel.send('tu contrasenia:' + gen_pass(10))

client.run("TOKEN")
