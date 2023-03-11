import pytest
import janisbot4.plugins.quote_command as quote_command

from janisbot4.config import cfg
from tests.message_stub import MessageStub


@pytest.mark.asyncio
async def test_quote_is_returned_on_command(requests_mock):
    expected = "test quote"
    reply = [{"quote": expected}]
    url = cfg.get("quote_api_url") + "/random_quotes?limit=1"

    requests_mock.get(url, json=reply)

    message_stub = MessageStub()

    await quote_command.index(message_stub)
    assert message_stub.replied == expected
