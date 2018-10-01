import discord
from profanityfilter import ProfanityFilter

p = ProfanityFilter()

TOKEN = 'NDk1NzAyNzQxOTQzOTc1OTM3.DpGz6w.uhfwQsrro2IqZ1mCjuLFos8_3ms'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    m = message.content
    if p.is_clean(m):
        pass
    else:
        await client.delete_message(message)
        mesg = 'Your message has been deleted because it contains profanity {0.author.mention}'.format(message)
        await client.send_message(message.channel, mesg)
    

    if message.content.startswith('!help-antiswear'):
        msg = 'Hello, I am anti-swear bot. I was made to keep this a clean server and cursing-free'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!copyright-antiswear'):
        await client.send_message(message.channel, 'Copyright (C) Brian Zheng 2018, all rights reserved')


client.run(TOKEN)
