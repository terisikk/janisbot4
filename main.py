import os
from dotenv import load_dotenv

# Need to load before any imports, or module static variable loading from env does not work
load_dotenv(dotenv_path=os.environ.get("JANISBOT_CONFIG", "conf/prod_template.env"))

from aiogram import executor
import os
from janisbot4 import bot, config

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

if __name__ == "__main__":
    dispatcher = bot.create_bot(config.cfg.get("MODE"))
    executor.start_polling(dispatcher, skip_updates=True)
