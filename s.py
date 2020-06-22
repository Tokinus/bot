import discord, asyncio, random, requests, utils, datetime
from discord.ext import commands

#prefix
Bot = commands.Bot(command_prefix=';')     
Bot.remove_command('help')

@Bot.event
async def on_ready():
    while True:
        await Bot.change_presence(activity= discord.Activity(type= discord.ActivityType.watching, name=f"Порно эдинорогов|;help"), status= discord.Status.idle)
        await asyncio.sleep(10)
        await Bot.change_presence(activity= discord.Activity(type= discord.ActivityType.watching, name=f"За {len(Bot.guilds)} серверов|;help"), status= discord.Status.idle)
        await asyncio.sleep(10)
        await Bot.change_presence(activity= discord.Activity(type= discord.ActivityType.watching, name=f"За {len(Bot.users)} участников|;help"), status= discord.Status.dnd)
        await asyncio.sleep(10)

# Stats bot
@Bot.command()
async def info(ctx):
    embed = discord.Embed(title="Имя бота", description=" Frost bot", color=0xeee657)
    embed.add_field(name="Создатель бота", value="Tokinus#3395")
    embed.add_field(name="Находится на количество серверов", value=f"{len(Bot.guilds)}")
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
    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top role:", value=member.top_role.mention)
    embed.add_field(name="Bot?", value=member.bot)
    await ctx.send(embed=embed)

#serverinfo
@Bot.command()
async def serverinfo(ctx):
    embed = discord.Embed(colour=0xff8040)
    embed.set_author(name=f"Информация о сервере {ctx.guild.name}")
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name="Создатель:",value=ctx.guild.owner_id)
    embed.add_field(name="ID:",value=ctx.guild.id)
    embed.add_field(name="Регион:",value=ctx.guild.region)
    embed.add_field(name="Безопасность сервера",value=ctx.guild.verification_level)
    await ctx.send(embed=embed)

#Отправляет сообщение от имени бота
@Bot.command()
async def say(ctx): 
    #colors = random.choice(colours)
    await ctx.message.delete()
    emb = discord.Embed(title= None, description= "**{}**".format(ctx.message.content[4:]))
    emb.set_author(name=f"{ctx.author}")
    emb.set_footer(text=f"Вызван пользователям {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed = emb)

#sta
@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def mute(ctx,member:discord.Member,time:float, arg: str, *,reason):
    role = discord.utils.get(ctx.guild.roles,id=674257533828988938)
    channel = Bot.get_channel(674193647012413452)
    await member.add_roles(role)
    emb = discord.Embed(title="Блокировка Чата 🙊",color=0xff0000)
    emb.add_field(name='Администратор:',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель:',value=member.mention,inline=False)
    emb.add_field(name="Время:",value=time,inline=False)
    emb.add_field(name='Причина:',value=reason,inline=False)
    await channel.send(embed = emb)
    await asyncio.sleep(time * 60)
    if role in member.roles:
      emb = discord.Embed(title="Разблокировка Чата 🐵",color=0xff0000)
      emb.add_field(name='Администратор:',value=ctx.message.author.mention,inline=False)
      emb.add_field(name='Нарушитель:',value=member.mention,inline=False)
      emb.add_field(name='Причина:',value="Время мута вышло",inline=False)
      await channel.send(embed=emb)
      if arg =='s':
        await asyncio.sleep(time)
      elif arg =='m':
        await asyncio.sleep(time * 60)
      elif arg =='h':
        await asyncio.sleep(time * 60 * 60)
      elif arg =='d':
         await asyncio.sleep(time * 60 * 60 * 24)
      await member.remove_roles(role)

@Bot.command()
async def avatar(ctx, *,  member : discord.Member=None):
    userAvatarUrl = member.avatar_url
    await ctx.send(userAvatarUrl)


# connect
token = open ('token.txt', 'r' ).readline()
Bot.run(token)