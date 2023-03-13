from collections import namedtuple

Chat = namedtuple("Chat", "id")


class MessageStub:
    def __init__(self):
        self.replied = None
        self.chat = None
        self.args = "test is mine"
        self.text = "this is a test"
        self.from_user = UserStub()
        self.chat = ChatStub()

    async def reply(self, message, **kwargs):
        self.replied = message

    def get_args(self):
        return self.args


class UserStub:
    def __init__(self):
        self.username = "Test User"
        self.full_name = "Test User Full"


class ChatStub:
    def __init__(self):
        self.title = "Test Chat"
        self.full_name = "Full test chat name"
