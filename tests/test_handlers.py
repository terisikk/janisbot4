import pytest
import janisbot4.handlers as handlers

from janisbot4.config import cfg


class MessageStub():

    replied = None

    async def reply(self, message, **kwargs):
        self.replied = message

    def get_args(self):
        return 'test is mine'


@pytest.mark.asyncio
async def test_quote_is_returned_on_command(requests_mock):
    expected = 'test quote'
    reply = [{'quote': expected}]
    url = cfg.get('quote_api_url') + '/random_quotes?limit=1'

    requests_mock.get(url, json=reply)

    message_stub = MessageStub()

    await handlers.quote_command(message_stub)
    assert message_stub.replied == expected


@pytest.mark.asyncio
async def test_quote_is_returned_on_message(requests_mock):
    expected = 'test quote'
    reply = [{'quote': expected}]
    url = cfg.get('quote_api_url') + '/random_quotes?limit=1'

    requests_mock.get(url, json=reply)

    message_stub = MessageStub()

    await handlers.quote_message(message_stub)
    assert message_stub.replied == expected
