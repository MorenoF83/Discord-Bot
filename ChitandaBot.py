import discord
from discord.ext import commands
from typing import Optional
import random
import math
import time
from selenium import webdriver

TOKEN = 'NzIyNjE3MjYyMzc2MzUzODIz.XulsdQ.oTAr3p9BSxdXv_gYwdjtIR0w31o'

bot = commands.Bot(command_prefix='!')  # sets command prefix
bot.case_insensitive = True

#----------------EVENT FUNCTIONS----------------
#Performs function on start and notifies its ON and changes Discord activity
@bot.event
async def on_ready():
    #Changes Activity
    activity = discord.Activity(name='Hyouka LOL', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)

#Performs if Error occurs
@bot.event
async def on_command_error(ctx, error):
    pass

#Mentions in server when ON
#TO DO: Not need channel ID
@bot.event
async def on_connect():
    print("ON")
    await bot.get_channel(689206153883680814).send('Online')

#Mentions in server when OFF
#TO DO: Not need channel ID
@bot.event
async def on_disconnect():
    print("OFF")
    await bot.get_channel(689206153883680814).send('Offline')

#----------------COMMAND FUNCTIONS----------------
#Test command
@bot.command(name='test')
async def test(ctx, *, message: str):
    print('Test Command Used')
    await ctx.send(message)

#Help command
@bot.command(name='helping')
async def helping(ctx):
    print('Help Command Used')
    user = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name="!test", value = "Random test command", inline = False)

    await bot.send_message(user, embed=embed)

#Say hello to user typing !hello
@bot.command(name='hello')
async def hello(ctx):
    print('Hello Command Used')
    await ctx.send('Hello!')

#Flips coin after typing !flip
@bot.command(name='flip')
async def flip(ctx):
    sides = ['Heads', 'Tails']
    result = random.choice(sides)
    print('Flip Command Used')
    await ctx.send(result)

#Divides given names into different teams
@bot.command(name='team')
async def team(ctx, *, message: str):
    print('Team Command Used')
    inputUser = message
    list = inputUser.split()
    numOfTeams = int(list[0])
    list = list[1:]
    maxSize = math.ceil(len(list) / numOfTeams)
    tempList = list
    teamNum = 1
    output = ""
    for y in range(numOfTeams):
        output += ('TEAM ' + str(teamNum) + ':\n')
        for x in range(maxSize):
            if tempList:
                randomPerson = random.choice(tempList)
                output += (randomPerson + " ")
                tempList.remove(randomPerson)
        output += "\n"
        teamNum += 1
    await ctx.send(output)

#Sends picture
@bot.command(name="picture")
async def picture(ctx):
    print('Picture Command Used 2')
    await ctx.send(file=discord.File('C:\Coding stuff\screenshot.png'))

#U.GG Command of Build
@bot.command(name="build")
async def build(ctx, *, message: str):
    print('Build Command Used')
    list = message.split()
    PATH = "C:\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    website = 'https://u.gg/lol/champions/' + list[0] + '/build?role=' + list[1]
    driver.get(website)
    time.sleep(5)
    driver.save_screenshot("screenshot.png")
    driver.quit()
    await ctx.send(file=discord.File('C:\Coding stuff\Discord Bot\screenshot.png'))
bot.run(TOKEN)