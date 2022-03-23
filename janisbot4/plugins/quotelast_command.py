from janisbot4.quote_api import quotelast


COMMANDS = ['quotelast']


async def index(message):
    """
    Save the message replied to.
    """
    reply = message.reply_to_message
    if not reply:
        return

    quote = reply.text
    victim = get_user_name(reply)
    adder = get_user_name(message)

    channel = message.chat.title or message.chat.full_name

    if filter_quote_message(quote) or filter_lorrem(quote):
        return

    quotelast(channel, quote, victim, adder)


def get_user_name(message):
    return message.from_user.username if message.from_user.username else message.from_user.full_name


def filter_lorrem(text):
    return str.startswith(text, "[LÖR]")


def filter_quote_message(text):
    return str.endswith(text, ":")
