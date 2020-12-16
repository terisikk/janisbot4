from collections import namedtuple

Chat = namedtuple('Chat', 'id')


class MessageStub():

    def __init__(self):
        self.replied = None
        self.chat = None
        self.args = 'test is mine'

    async def reply(self, message, **kwargs):
        self.replied = message

    def get_args(self):
        return self.args
