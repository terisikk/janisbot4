from janisbot4.api.quote_api import get_quote_count

COMMANDS = ["quotecunt"]


async def index(message):
    arguments = message.get_args()
    await message.reply(get_quote_count(user=arguments), reply=False)
