import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'🎮 Bot de juegos listo!')

# COMANDOS
@bot.command()
async def dado(ctx, caras: int = 6):
    """Tira un dado (1-6 por defecto)"""
    if caras < 2:
        await ctx.send("❌ El dado debe tener al menos 2 caras")
        return
    
    resultado = random.randint(1, caras)
    await ctx.send(f"🎲 {ctx.author.mention} tiró un dado de **{caras}** caras: **{resultado}**")

@bot.command()
async def moneda(ctx):
    """Lanza una moneda"""
    resultado = random.choice(["Cara 👑", "Cruz ⚔️"])
    await ctx.send(f"🪙 {ctx.author.mention} lanzó una moneda: **{resultado}**")

@bot.command()
async def abrazo(ctx, miembro: discord.Member = None):
    """Abraza a alguien"""
    if miembro is None:
        await ctx.send("❌ Debes mencionar a alguien para abrazar")
        return
    
    if miembro == ctx.author:
        await ctx.send("🤔 No puedes abrazarte a ti mismo...")
        return
    
    mensajes_abrazo = [
        f"🤗 {ctx.author.mention} abrazó fuertemente a {miembro.mention}",
        f"💕 {ctx.author.mention} le da un caluroso abrazo a {miembro.mention}",
        f"❤️ {ctx.author.mention} abraza a {miembro.mention} con mucho cariño"
    ]
    
    await ctx.send(random.choice(mensajes_abrazo))

@bot.command()
async def chiste(ctx):
    """Cuenta un chiste aleatorio"""
    chistes = [
        "¿Por qué los pájaros vuelan sur? ⬇️ Porque caminando tardarían mucho. 🐦",
        "¿Qué le dice un jamón a otro jamón? 🐷 ¡Nos vemos en el jamón!",
        "¿Cómo se llama el campeón de buceo japonés? 🏊 Toko sentado.",
        "¿Qué hace una abeja en el gimnasio? 🐝 ¡Zum-ba!",
        "¿Por qué Superman no necesita internet? 🦸‍♂️ Porque ya tiene Supernet."
    ]
    
    await ctx.send(random.choice(chistes))

answers = ["Sí", "No", "Tal vez", "Pregunta después", "Definitivamente", "No tengo idea"]

@bot.command(name="8ball")
async def eightball(ctx, *, question: str):
    await ctx.send(random.choice(answers))
    
bot.run("TOKEN")

