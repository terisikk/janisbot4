from janisbot4.bot import create_bot, get_api_server, PRODUCTION, TEST

from aiogram import Bot
from aiogram.dispatcher import Dispatcher


def test_create_bot_can_be_created():
    dp, bot = create_bot("unknown")

    assert isinstance(bot, Bot)
    assert isinstance(dp, Dispatcher)

    assert len(dp.message_handlers.handlers) > 0


def test_api_server_returns_test_server_in_tests():
    server = get_api_server(TEST)

    assert "/test/" in server.base


def test_api_server_returns_prod_server_in_prod():
    server = get_api_server(PRODUCTION)

    assert server.base.startswith("https://api.telegram.org/")
