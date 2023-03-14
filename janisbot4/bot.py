import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters.builtin import IDFilter
from aiogram.bot.api import TelegramAPIServer

from janisbot4.config import cfg
from janisbot4 import plugin_loader, plugins

TELEGRAM_API_TOKEN = cfg.get("TELEGRAM_API_TOKEN")
USER_IDS = cfg.get("USER_IDS").split(",") if cfg.get("USER_IDS") else None
CHAT_IDS = cfg.get("CHAT_IDS").split(",") if cfg.get("USER_IDS") else None
PRODUCTION = "prod"
TEST = "test"
LOGGER_NAME = "janisbot"

botlogger = logging.getLogger(LOGGER_NAME)
botlogger.setLevel(int(os.environ.get("JANISBOT_LOGLEVEL", logging.DEBUG)))


def get_api_server(mode):
    if mode == PRODUCTION:
        return TelegramAPIServer.from_base("https://api.telegram.org/")
    else:
        return TelegramAPIServer(
            base="https://api.telegram.org/bot{token}/test/{method}",
            file="https://api.telegram.org/file/bot{token}/test/{path}",
        )


def create_bot(mode):
    bot = Bot(token=TELEGRAM_API_TOKEN, server=get_api_server(mode))

    dp = Dispatcher(bot)

    idfilter = IDFilter(user_id=USER_IDS, chat_id=CHAT_IDS)

    plugin_loader.register_plugins(plugin_loader.load_plugins(plugins.__path__[0]), dp, idfilter)

    return (dp, bot)
