import pytest
import janisbot4.handlers as handlers

from janisbot4.config import cfg
from tests.message_stub import MessageStub


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


@pytest.mark.asyncio
async def test_random_choice_is_returned_on_command(requests_mock):
    expected = ['choice1', 'choice2', 'choice3']

    message_stub = MessageStub()
    message_stub.args = "choice1 choice2 choice3"

    await handlers.randchoice_command(message_stub)
    assert message_stub.replied in expected


@pytest.mark.asyncio
async def test_randchoice_does_not_split_phrases():
    expected = "This is the choice"

    message_stub = MessageStub()
    message_stub.args = "'This is the choice'"

    await handlers.randchoice_command(message_stub)
    assert message_stub.replied in expected


@pytest.mark.asyncio
async def test_quotelast_api_is_called_from_handler(requests_mock):
    url = cfg.get('quote_api_url') + '/rpc/quotelast'

    message_stub = MessageStub()
    message_stub.reply_to_message = MessageStub()
    message_stub.reply_to_message.args = "test quote"

    adapter = requests_mock.post(url)
    await handlers.quotelast_command(message_stub)

    assert adapter.called


@pytest.mark.asyncio
async def test_quotelast_api_is_not_called_without_reply(requests_mock):
    url = cfg.get('quote_api_url') + '/rpc/quotelast'

    message_stub = MessageStub()
    message_stub.reply_to_message = None

    adapter = requests_mock.post(url)
    await handlers.quotelast_command(message_stub)

    assert adapter.called is False
