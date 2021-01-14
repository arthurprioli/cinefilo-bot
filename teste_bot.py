import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-setfilme'):
        global filme
        filme = message.content.lstrip('-setfilme')
        await message.channel.send('O filme de hoje agora é:{0}'.format(filme))

    if message.content.startswith('-filme'):
        await message.channel.send('O filme de hoje é:{0}'.format(filme))
        
    if message.content.startswith('-trailer'):
        await message.channel.send('-play {0} trailer'.format(filme))
        
        

@client.event
async def on_join(self, member):
    guild = member.guild
    if guild.system.channel is not None:
        await guild.system_channel.send('Bem vindo {0.mention} ao {1.name}'.format(member, guild))

client.run(TOKEN)
