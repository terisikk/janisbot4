import pytest
import janisbot4.plugins.quote_message as quote_message

from janisbot4.config import cfg
from tests.unit.message_stub import MessageStub


@pytest.mark.asyncio
async def test_quote_is_returned_on_message(requests_mock):
    expected = "test quote"
    reply = [{"quote": expected}]
    url = cfg.get("QUOTE_API_URL") + "/random_quotes?limit=1"

    requests_mock.get(url, json=reply)  # nosec B113

    message_stub = MessageStub()

    await quote_message.index(message_stub)
    assert message_stub.replied == expected
