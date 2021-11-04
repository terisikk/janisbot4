import logging
import os
import janisbot4.handlers as handlers

from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters.builtin import IDFilter
from janisbot4.config import cfg


TELEGRAM_API_TOKEN = cfg.get('telegram_api_token')

# Configure logging
logging.basicConfig(level=int(os.environ.get('JANISBOT_LOGLEVEL', logging.INFO)))

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)

idFilter = IDFilter(user_id=cfg.get('user_ids'), chat_id=cfg.get('chat_ids'))

dp.register_message_handler(handlers.quote_command, idFilter, commands=['quote'])
dp.register_message_handler(handlers.quotelast_command, idFilter, commands=['quotelast'])
dp.register_message_handler(handlers.quote_message, idFilter, regexp='.*:$')

dp.register_message_handler(handlers.randchoice_command, idFilter, commands=['randchoice'])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
