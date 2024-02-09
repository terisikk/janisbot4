import asyncio
import socket

import pytest_asyncio
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

import janisbot4.bot
from janisbot4.config import cfg

TELEGRAM_API_DEV_ID = cfg.get("TELEGRAM_API_DEV_ID")
TELEGRAM_API_DEV_HASH = cfg.get("TELEGRAM_API_DEV_HASH")
TELEGRAM_CLIENT_SESSION = cfg.get("TELEGRAM_CLIENT_SESSION")
TELEGRAM_TEST_DC_IP = cfg.get("TELEGRAM_TEST_DC_IP")
TELEGRAM_TEST_DC_NUMBER = cfg.get("TELEGRAM_TESTS_DC_NUMBER")
TELEGRAM_TEST_DC_PORT = cfg.get("TELEGRAM_TEST_DC_PORT", 443)


@pytest_asyncio.fixture(scope="module")
async def bot(event_loop):
    dp, bot = janisbot4.bot.create_bot(janisbot4.bot.TEST)
    task = event_loop.create_task(dp.start_polling())

    yield task

    task.cancel()
    await (await bot.get_session()).close()
    dp.stop_polling()

    # TODO: I don't know how to properly run asyncio, without this the loop is
    # destroyed before the task is cancelled
    await asyncio.sleep(1)


@pytest_asyncio.fixture(scope="module")
async def telegram_client():
    session = StringSession(TELEGRAM_CLIENT_SESSION)
    session.set_dc(TELEGRAM_TEST_DC_NUMBER, TELEGRAM_TEST_DC_IP, TELEGRAM_TEST_DC_PORT)

    async with TelegramClient(session, TELEGRAM_API_DEV_ID, TELEGRAM_API_DEV_HASH, sequential_updates=True) as client:
        yield client


@pytest_asyncio.fixture(scope="module")
async def conv(bot, telegram_client):
    async with telegram_client.conversation("@TestJanisBot", timeout=30, max_messages=100) as conv:
        await conv.send_message(f"Starting E2E tests from {socket.gethostname()}...")
        yield conv
        await conv.send_message("E2E tests done.")


# Default event_loop fixture has "function" scope and will
# through ScopeMismatch exception since there are related
# fixtures with "session" scope. Need to override to set scope.
# https://github.com/pytest-dev/pytest-asyncio#event_loop
@pytest_asyncio.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()
