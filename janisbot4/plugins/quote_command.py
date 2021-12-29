from janisbot4.quote_api import get_random_quote


def register(dispatcher, idfilter=None):
    dispatcher.register_message_handler(index, idfilter, commands=['quote'])


async def index(message):
    arguments = message.get_args().split(' ')
    await message.reply(get_random_quote(arguments), reply=False)
