import discord
from bot_logic import gen_pass
from  Moneda_bot import Moneda

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Hemos iniciado sesión como {client.user}')
    print('El bot está listo para usar!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("👋")
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(pass_length=12))
    elif message.content.startswith('$moneda'): 
        await message.channel.send(Moneda())
    else:
        await message.channel.send(message.content)

TOKEN = "MTQwMjA3MzkxMzUyNTAxNDYzMA.Gb3ce1.sSCIQ681HhHz77adriE3tfTYdLro2G_m1NqUrY"

try:
    client.run(TOKEN)
except discord.LoginFailure:
    print("❌ Error: Token inválido. ¿Regeneraste el token?")
    input("Presiona Enter para cerrar...")
except discord.HTTPException as e:
    print(f"❌ Error HTTP: {e}")
    input("Presiona Enter para cerrar...")
except Exception as e:
    print(f"❌ Error inesperado: {e}")
    input("Presiona Enter para cerrar...")