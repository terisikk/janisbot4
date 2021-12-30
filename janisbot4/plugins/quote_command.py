from janisbot4.quote_api import get_random_quote


COMMANDS = ['quote']


async def index(message):
    arguments = message.get_args().split(' ')
    await message.reply(get_random_quote(arguments), reply=False)
