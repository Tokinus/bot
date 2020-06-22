import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as DT                          
from time import sleep                          
import os
from discord.utils import get
from re import search
import utils
import random
from Cybernator import Paginator
import requests

#prefix
Bot = commands.Bot(command_prefix=';')     
Bot.remove_command('help')

# Stats bot
@Bot.command()
async def info(ctx):
    embed = discord.Embed(title="Название Бота", description="Frost Bot", color=0xeee657)
    
    # give info about you here
    embed.add_field(name="Создатель бота", value="Tokinus#3395")

    #avatar
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Находится на количество серверов", value=f"{len(Bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Добавить бота", value="https://discord.com/api/oauth2/authorize?client_id=703983771111915520&permissions=0&scope=bot")

    await ctx.send(embed=embed)

#userinfo
@Bot.command()
async def userinfo(ctx, member: discord.Member):
 
    roles = [role for role in member.roles]
 
    embed = discord.Embed(colour=member.color)
 
    embed.set_author(name=f"Информация о пользователя - {member}")
    embed.set_thumbnail(url=member.avatar_url)
 
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Никнейм", value=member.display_name)
 
    embed.add_field(name="Создал в:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Присойденился:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
 
    embed.add_field(name="Роль:", value=member.top_role.mention)
 
    await ctx.send(embed=embed)

#serverinfo
@Bot.command()
async def serverinfo(ctx):

    embed = discord.Embed(colour=0xff8040)

    embed.set_author(name=f"Информация о сервере {ctx.guild.name}")
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name="Создатель:",value=ctx.guild.owner)
    embed.add_field(name="ID:",value=ctx.guild.id)

    embed.add_field(name="Регион:",value=ctx.guild.region)
    embed.add_field(name="Безопасность сервера:",value=ctx.guild.verification_level)

    embed.add_field(name="Участников:",value=ctx.guild.members)

    await ctx.send(embed=embed)

@Bot.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

#Отправляет сообщение от имени бота
@Bot.command()
async def say(ctx): 
    #colors = random.choice(colours)
    await ctx.message.delete()
    emb = discord.Embed(title= None, description= "**{}**".format(ctx.message.content[4:]))
    emb.set_author(name="Система say")
    emb.set_footer(text=f"Вызван пользователям {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed = emb)

#help
@Bot.command()
async def help(ctx):
    embed=discord.Embed(title="Информация о командах | ;help", color=0xff8000)
    embed.add_field(name="info ", value="показывает информацию о Бота", inline=False)
    embed.add_field(name="userinfo (имя пользователя)", value="Показывает информацию о пользователя которого вы упомянули", inline=True)
    embed.add_field(name="serverinfo", value="Показывает информацию о сервере", inline=True)
    embed.add_field(name="avatar (имя пользователя)", value="Показывает аватар пользователя которого упомянули", inline=True)
    embed.add_field(name="скоро добавлю больше команд ", value="спасибо что вы добавили моего бота на свой сервер", inline=True)
    await Bot.say(embed=embed)



@Bot.event
async def on_ready():
    guilds = len(Bot.guilds)
    while True:
        await Bot.change_presence(activity= discord.Activity(type= discord.ActivityType.watching, name= "guilds"), status= discord.Status.online)
        await asyncio.sleep(10)
        await Bot.change_presence(activity= discord.Activity(type= discord.ActivityType.watching, name= "Второе значение", status= discord.Status.online)
        await asyncio.sleep(11)
        await Bot.change_presence(activity= discord.Activity(type= discord.ActivityType.watching, name= "Тff значение"), status= discord.Status.online)
        await asyncio.sleep(12)
    # connect
token = open ('token.txt', 'r' ).readline()
Bot.run(token)
