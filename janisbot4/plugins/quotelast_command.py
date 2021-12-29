from janisbot4.quote_api import quotelast


def register(dispatcher, idfilter=None):
    dispatcher.register_message_handler(index, idfilter, commands=['quotelast'])


async def index(message):
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


def filter_lorrem(text):
    return str.startswith(text, "[LÖR]")


def filter_quote_message(text):
    return str.endswith(text, ":")
