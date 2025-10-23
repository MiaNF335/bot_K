import discord, os, random, requests
from discord.ext import commands

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
async def mem(ctx):
    if os.path.exists("images"):
        # Obtener lista de archivos en la carpeta
        archivos = os.listdir('images')
        if len(archivos) == 0:
            await ctx.send("La carpeta 'images' está vacía.")
            return

        # Elegir un archivo al azar
        img_name = random.choice(archivos)

        # Abrir y enviar el archivo
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)

        print("Imagen enviada:", img_name)
    else:
        await ctx.send("La carpeta 'images' no existe.")

@bot.command()
async def animal(ctx):
    if os.path.exists('animals'):
        archivos = os.listdir('animals')
        if len(archivos) == 0:
            await ctx.send('la carpeta "animals" esta vacia. ')
            return
        
        img_name = random.choice(archivos)

        with open(f'animals/{img_name}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)

        print('imagen enviada:', img_name)
    else:
        await ctx.send('La carpeta "animals" no existe.')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()

bot.run('token here')
    await ctx.send(image_url)
