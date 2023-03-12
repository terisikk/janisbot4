import logging
import os

from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters.builtin import IDFilter

from janisbot4.config import cfg
from janisbot4 import plugin_loader, plugins

TELEGRAM_API_TOKEN = cfg.get("telegram_api_token")

logging.basicConfig(level=int(os.environ.get("JANISBOT_LOGLEVEL", logging.INFO)))

bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)

idfilter = IDFilter(user_id=cfg.get("user_ids"), chat_id=cfg.get("chat_ids"))

plugin_loader.register_plugins(plugin_loader.load_plugins(plugins.__path__[0]), dp, idfilter)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
