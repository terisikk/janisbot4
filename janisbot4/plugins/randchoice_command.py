import shlex

from random import choice
from aiogram.dispatcher.filters.builtin import IDFilter

from janisbot4.config import cfg


idFilter = IDFilter(user_id=cfg.get('user_ids'), chat_id=cfg.get('chat_ids'))


def register(dispatcher):
    dispatcher.register_message_handler(index, idFilter, commands=['randchoice'])


async def index(message):
    arguments = shlex.split(message.get_args())
    await message.reply(choice(arguments), reply=True)
