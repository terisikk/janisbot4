from aiogram.dispatcher.filters.builtin import IDFilter

from janisbot4.quote_api import get_random_quote
from janisbot4.config import cfg


idFilter = IDFilter(user_id=cfg.get('user_ids'), chat_id=cfg.get('chat_ids'))


def register(dispatcher):
    dispatcher.register_message_handler(index, idFilter, regexp='.*:$')


async def index(message):
    await message.reply(get_random_quote(), reply=False)
