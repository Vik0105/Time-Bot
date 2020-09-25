from datetime import datetime
from dateutil import tz
import discord
from discord.ext import commands
import asyncio

botPrefix = "" #Your Prefix Here
botToken = "" #Your Bot Token Here

bot=commands.Bot(command_prefix=botPrefix)
t = "Asia/Dubai"
timeZone = tz.gettz(t) if t is not None else tz.tzutc()


@bot.event
async def on_ready():
    print("Logged in as "+bot.user.name)
    while True:
      await ctx.guild.me.edit(nick=datetime.now().astimezone(timeZone).strftime("%a %I:%M %p"))
      await asyncio.sleep(300) #changes time every 5 minutes
      await ctx.guild.me.edit(nick=datetime.now().astimezone(timeZone).strftime("%a %I:%M %p"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #Change timezone with !timezone [zone]
    if message.content.startswith('!timezone'):
        omsg = message.content
        t = search.replace('!timezone ', '')
        await message.channel.send('Timezone Changed!')
    
bot.run(botToken)
