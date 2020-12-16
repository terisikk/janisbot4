from janisbot4.quote_api import get_random_quote
from random import choice


async def quote_command(message):
    arguments = message.get_args().split(' ')
    await message.reply(get_random_quote(arguments), reply=False)


async def quote_message(message):
    await message.reply(get_random_quote(), reply=False)


async def randchoice_command(message):
    arguments = message.get_args().split(' ')
    await message.reply(choice(arguments), reply=True)
