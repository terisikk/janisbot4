from aiogram import executor
from janisbot4 import bot, config

if __name__ == "__main__":
    dispatcher = bot.create_bot(config.cfg.get("mode"))
    executor.start_polling(dispatcher, skip_updates=True)
