import discord
from discord.ext import commands

prefix = "*" #you can change the prefix here
bot = commands.Bot(command_prefix = prefix)
MAGIC_CHAR = '\u202b'

@bot.event
async def on_ready():
    print("it's ready")
    
@bot.command
async def editglitch(ctx, message):
	await ctx.message.delete()
    	msg = await ctx.send(message)
	await msg.edit(content=f"{MAGIC_CHAR} {message} {MAGIC_CHAR}")
                       
bot.run("ur gay token", bot=False)
