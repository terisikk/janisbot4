import os
from dotenv import load_dotenv
from aiogram import executor

# Need to load before any janisbot4 imports, or module static variable loading from env does not work
load_dotenv(dotenv_path=os.environ.get("JANISBOT_CONFIG", "conf/prod_template.env"))

from janisbot4 import bot, config  # noqa: E402

if __name__ == "__main__":
    dispatcher, _ = bot.create_bot(config.cfg.get("MODE"))
    executor.start_polling(dispatcher, skip_updates=True)
