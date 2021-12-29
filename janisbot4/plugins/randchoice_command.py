import shlex

from random import choice


def register(dispatcher, idfilter=None):
    dispatcher.register_message_handler(index, idfilter, commands=['randchoice'])


async def index(message):
    arguments = shlex.split(message.get_args())
    await message.reply(choice(arguments), reply=True)
