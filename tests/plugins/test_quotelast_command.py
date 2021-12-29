import pytest

from janisbot4.plugins import quotelast_command
from janisbot4.config import cfg

from tests.message_stub import MessageStub
from tests.dispatcher_stub import DispatcherStub


def test_command_can_be_registered():
    dispatcher = DispatcherStub()

    quotelast_command.register(dispatcher)
    assert dispatcher.called


@pytest.mark.asyncio
async def test_quotelast_api_is_called_from_handler(requests_mock):
    url = cfg.get('quote_api_url') + '/rpc/quotelast'

    message_stub = MessageStub()
    message_stub.reply_to_message = MessageStub()
    message_stub.reply_to_message.text = "test quote"

    adapter = requests_mock.post(url)
    await quotelast_command.index(message_stub)

    assert adapter.called


@pytest.mark.asyncio
async def test_quotelast_api_is_not_called_without_reply(requests_mock):
    url = cfg.get('quote_api_url') + '/rpc/quotelast'

    message_stub = MessageStub()
    message_stub.reply_to_message = None

    adapter = requests_mock.post(url)
    await quotelast_command.index(message_stub)

    assert adapter.called is False


@pytest.mark.parametrize('text', ["[LÖR] filter me", "filter me:"])
@pytest.mark.asyncio
async def test_quotelast_is_filtered_by_rules(requests_mock, text):
    url = cfg.get('quote_api_url') + '/rpc/quotelast'

    message_stub = MessageStub()
    message_stub.reply_to_message = MessageStub()
    message_stub.reply_to_message.text = text

    adapter = requests_mock.post(url)
    await quotelast_command.index(message_stub)

    assert adapter.called is False
