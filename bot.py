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

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
    
        
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="pa-speaker")
    await channel.send(f"{member} has arrived!")

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