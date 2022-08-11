import os
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(
	command_prefix="!", 
	case_insensitive=True  
)

bot.author_id = 487258918465306634 #put your discord id here


@bot.command()
async def test(ctx):
    await ctx.send('test')


@bot.event 
async def on_ready():  
    print("I'm in")
    print(bot.user)  


extensions = [
	'cogs.cog_example'  
]

if __name__ == '__main__':  
	for extension in extensions:
		bot.load_extension(extension) 

keep_alive()  
token = os.environ.get("TOKEN") #put your bot token were it says "TOKEN"
bot.run(token)  