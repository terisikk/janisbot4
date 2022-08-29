from janisbot4.lorrem_api import get_random_lorr


COMMANDS = ['lorr']


async def index(message):
    await message.reply(get_random_lorr(), reply=False)
