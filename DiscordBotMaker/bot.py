import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='')


@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(''))
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')


@bot.command()
async def sayhi(ctx):
	await ctx.send('hi')

bot.run('')