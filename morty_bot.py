from ast import alias
import asyncio
import discord
from discord.ext import commands

import sqlite3

from threading import Thread
from discord.ext import tasks
from itertools import cycle


rick_list = []
morty_list = []
intents = discord.Intents().all()

bot = commands.Bot(command_prefix="n?",
intents = intents,
case_insensitive=False,
)
bot.remove_command('help')

status = cycle(['cooking shooking','space travel with rick'])

@bot.event
async def on_ready():
                print("My name is {0.user} and i am ready to go".format(bot))
                change_status.start()
                print("Your bot is ready")
                conn_morty = sqlite3.connect('mortydata.sqlite')
                cur_morty = conn_morty.cursor()
                cur_morty.execute('SELECT line FROM mortylines ORDER BY rank ASC')
                line_morty = cur_morty.fetchall()
                for i in line_morty :
                        morty_list.append(i[0])
                conn_rick = sqlite3.connect('rickdata.sqlite')
                cur_rick = conn_rick.cursor()
                line_rick = cur_rick.fetchall()
                for j in line_rick :
                        rick_list.append(j[0])
    
    


@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))


@bot.event
async def on_message(message) : 
        if int(message.author.id)  == "RICK BOT ID" :
                for i in rick_list : 
                        if message == str(i) :
                                rick_index = rick_list.index(i)
                                asyncio.sleep(2)
                                await message.channel.send(morty_list[rick_index])
                                break
                        else :

                                continue
        else :
            await bot.process_commands(message)

bot.run('TOKEN')
