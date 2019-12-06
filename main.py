import logging
import os
import janisbot4.handlers as handlers

from aiogram import Bot, Dispatcher, executor
from janisbot4.config import cfg
from janisbot4.filters import ChatIdFilter


TELEGRAM_API_TOKEN = cfg.get('telegram_api_token')

# Configure logging
logging.basicConfig(level=int(os.environ.get('JANISBOT_LOGLEVEL', logging.INFO)))

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)

chat_id_filter = ChatIdFilter(cfg.get('chat_ids'))

dp.register_message_handler(handlers.quote_command, chat_id_filter, commands=['quote'])
dp.register_message_handler(handlers.quote_message, chat_id_filter, regexp='.*:$')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
