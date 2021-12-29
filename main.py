import logging
import os
from janisbot4.plugins import quote_command, quote_message, quotelast_command, randchoice_command

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

quote_command.register(dp)
quote_message.register(dp)
quotelast_command.register(dp)
randchoice_command.register(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
