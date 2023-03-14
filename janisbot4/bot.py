import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters.builtin import IDFilter
from aiogram.bot.api import TelegramAPIServer

from janisbot4.config import cfg
from janisbot4 import plugin_loader, plugins

TELEGRAM_API_TOKEN = cfg.get("TELEGRAM_API_TOKEN")
LOGGER_NAME = "aiogram-logger"
USER_IDS = cfg.get("USER_IDS").split(",") if cfg.get("USER_IDS") else None
CHAT_IDS = cfg.get("USER_IDS").split(",") if cfg.get("USER_IDS") else None


bot_logger = logging.getLogger(LOGGER_NAME)
logging.basicConfig(level=int(os.environ.get("JANISBOT_LOGLEVEL", logging.DEBUG)))

PRODUCTION = "prod"
TEST = "test"


def get_api_server(mode):
    if mode == PRODUCTION:
        return TelegramAPIServer.from_base("https://api.telegram.org/")
    else:
        return TelegramAPIServer(
            base=f"https://api.telegram.org/bot{{token}}/test/{{method}}",
            file=f"https://api.telegram.org/file/bot{{token}}/test/{{path}}",
        )


def create_bot(mode, loop=None):
    bot = Bot(token=TELEGRAM_API_TOKEN, server=get_api_server(mode))

    dp = None

    if loop:
        dp = Dispatcher(bot, loop=loop)
    else:
        dp = Dispatcher(bot)

    idfilter = IDFilter(user_id=USER_IDS, chat_id=CHAT_IDS)

    plugin_loader.register_plugins(plugin_loader.load_plugins(plugins.__path__[0]), dp, idfilter)

    return (dp, bot)
