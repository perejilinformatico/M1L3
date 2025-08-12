import discord
from discord.ext import commands
from Moneda_bot import Moneda
from bot_logic import gen_pass

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
async def bye(ctx):
    await ctx.send(f'Adios, soy el bot: {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def sumar(ctx, num1: int, num2: int):
    resultado = num1 + num2 
    await ctx.send(f"La Suma de {num1} y {num2} es: {resultado}")

@bot.command()
async def restar(ctx, num1: int, num2: int):
    resultado = num1 - num2 
    await ctx.send(f"La Resta de {num1} y {num2} es: {resultado}")

@bot.command()
async def multiplicar(ctx,num1: int, num2: int):
    resultado = num1 * num2
    await ctx.send(f"La multiplicacion de {num1}  y {num2} es: {resultado}")

@bot.command()
async def dividir(ctx, num1: int, num2: int):
    if num2 == 0:
        await ctx.send("No se puede dividir por cero.")
    elif num1 == 0:
        await ctx.send("No se puede dividir cero entre un numero.")
    else:
        resultado = num1 / num2
        await ctx.send(f"La division de {num1} y {num2} es: {resultado}")

@bot.command()
async def moneda(ctx):
    await ctx.send(Moneda())

@bot.command()
async def contraseña(ctx):
    await ctx.send(gen_pass(pass_length=12))

bot.run("TOKEN")
