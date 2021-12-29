from janisbot4.quote_api import get_random_quote


def register(dispatcher, idfilter=None):
    dispatcher.register_message_handler(index, idfilter, regexp='.*:$')


async def index(message):
    await message.reply(get_random_quote(), reply=False)
