from discord.ext import commands, tasks
from dotenv import load_dotenv
import asyncio
import discord
import io
import os
import sys
from signal import SIGINT, SIGTERM

load_dotenv()
DISCORD_TOKEN = os.environ['DISCORD_TOKEN']

intents=discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
    
@client.event
async def on_message(message):
    if (message.channel.name == 'chill-vc-chat'):
    	print(message.author.name + ': ' + message.content.strip())

@client.event
async def on_member_join(member):
    print(member.name + " has joined!")
    # Use this if you have multiple servers. You can also just get the member.guild.text_channels
    # channel = discord.utils.get(member.guild.text_channels, name='chill-vc-chat')
    channel = discord.utils.get(client.get_all_channels(), name='chill-vc-chat')
    await channel.send(f"{member.mention} has arrived!")

client.run(DISCORD_TOKEN)


if __name__ == '__main__':
	if not DISCORD_TOKEN:
		print('Error: DISCORD_TOKEN not found')
		sys.exit(1)

	loop = asyncio.get_event_loop()

	def interrupt():
		raise KeyboardInterrupt

	loop.add_signal_handler(SIGINT, interrupt)
	loop.add_signal_handler(SIGTERM, interrupt)

	try:
		loop.run_until_complete(client.run(DISCORD_TOKEN))
	except KeyboardInterrupt:
		pass
	finally:
		loop.run_until_complete(client.close())