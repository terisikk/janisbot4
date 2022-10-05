from janisbot4.api.lorrem_api import get_random_lorr


COMMANDS = ['lorr']


async def index(message):
    await message.reply(get_random_lorr(), reply=False)
