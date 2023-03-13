import pytest
import re
import janisbot4.plugins.blame_command as blame_command

from janisbot4.config import cfg
from tests.unit.message_stub import MessageStub


@pytest.mark.asyncio
async def test_metadata_is_returned_on_command(requests_mock):
    expected = "Test User at #test by unknown adder, 2012-04-14T01:46:07"
    reply = [
        {"timestamp": "2012-04-14T01:46:07", "user": {"name": "Test User"}, "adder": None, "channel": {"name": "#test"}}
    ]
    url = re.compile(cfg.get("quote_api_url") + "/irc_quote.*")

    adapter = requests_mock.get(url, json=reply)

    message_stub = MessageStub()
    message_stub.reply_to_message = MessageStub()
    message_stub.reply_to_message.text = "test quote"

    await blame_command.index(message_stub)

    assert adapter.called
    assert message_stub.replied == expected


@pytest.mark.asyncio
async def test_blame_api_is_not_called_without_reply(requests_mock):
    url = re.compile(cfg.get("quote_api_url") + "/irc_quote.*")

    message_stub = MessageStub()
    message_stub.reply_to_message = None

    adapter = requests_mock.post(url)
    await blame_command.index(message_stub)

    assert adapter.called is False
