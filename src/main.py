import logging

from aiogram import Bot, Dispatcher, executor, types
from configurations import Configurations
from quote_api import get_random_quote

configs = Configurations('../conf/test.conf')

TELEGRAM_API_TOKEN = configs.get('telegram_api_token')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['quote'])
async def quotes_command(message: types.Message):
    await message.reply(get_random_quote(), reply=False)


@dp.message_handler(regexp='.*:')
async def quotes(message: types.Message):
    await message.reply(get_random_quote(), reply=False)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
