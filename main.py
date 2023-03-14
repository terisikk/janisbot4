from aiogram import executor
from dotenv import load_dotenv
import os
from janisbot4 import bot, config

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

if __name__ == "__main__":
    load_dotenv(dotenv_path=os.environ.get("JANISBOT_CONFIG", "conf/prod_template.env"))
    dispatcher = bot.create_bot(config.cfg.get("MODE"))
    executor.start_polling(dispatcher, skip_updates=True)
