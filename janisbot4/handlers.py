import shlex

from janisbot4.quote_api import get_random_quote, quotelast
from janisbot4.filters import filter_lorrem, filter_quote_message
from random import choice


async def quote_command(message):
    arguments = message.get_args().split(' ')
    await message.reply(get_random_quote(arguments), reply=False)


async def quote_message(message):
    await message.reply(get_random_quote(), reply=False)


async def randchoice_command(message):
    arguments = shlex.split(message.get_args())
    await message.reply(choice(arguments), reply=True)


async def quotelast_command(message):
    """
    Save the message replied to.
    """
    reply = message.reply_to_message
    if not reply:
        return

    quote = reply.text
    victim = reply.from_user.username
    adder = message.from_user.username

    channel = message.chat.title or message.chat.full_name

    if filter_quote_message(quote) or filter_lorrem(quote):
        return

    quotelast(channel, quote, victim, adder)
