from aiogram.dispatcher.filters import BoundFilter


class ChatIdFilter(BoundFilter):
    key = 'chat_ids'

    def __init__(self, chat_ids):
        if isinstance(chat_ids, int):
            chat_ids = [chat_ids]
        self.chat_ids = chat_ids

    async def check(self, message):
        return message.chat.id in self.chat_ids
