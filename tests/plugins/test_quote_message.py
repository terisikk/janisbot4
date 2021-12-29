import pytest
import janisbot4.plugins.quote_message as quote_message

from janisbot4.config import cfg
from tests.message_stub import MessageStub
from tests.dispatcher_stub import DispatcherStub


def test_command_can_be_registered():
    dispatcher = DispatcherStub()

    quote_message.register(dispatcher)
    assert dispatcher.called


@pytest.mark.asyncio
async def test_quote_is_returned_on_message(requests_mock):
    expected = 'test quote'
    reply = [{'quote': expected}]
    url = cfg.get('quote_api_url') + '/random_quotes?limit=1'

    requests_mock.get(url, json=reply)

    message_stub = MessageStub()

    await quote_message.index(message_stub)
    assert message_stub.replied == expected
