import shlex
from random import choice

COMMANDS = ["randchoice"]


async def index(message):
    arguments = shlex.split(message.get_args())
    await message.reply(choice(arguments), reply=True)  # noqa: S311
