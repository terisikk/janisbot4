import pytest
import janisbot4.plugins.quotecunt_command as quotecunt_command

from janisbot4.config import cfg
from tests.unit.message_stub import MessageStub


@pytest.mark.asyncio
async def test_total_count_is_returned_on_command(requests_mock):
    sata = 100
    reply = [{"count": sata}]
    url = cfg.get("QUOTE_API_URL") + "/quote_count"

    requests_mock.get(url, json=reply)  # nosec B113

    message_stub = MessageStub()
    message_stub.args = ""

    await quotecunt_command.index(message_stub)
    assert message_stub.replied == sata


@pytest.mark.asyncio
async def test_user_count_is_returned_on_command(requests_mock):
    expected = 100
    reply = [{"count": expected}]
    url = cfg.get("QUOTE_API_URL") + "/quotes_per_user?name=ilike.Test%20User"

    requests_mock.get(url, json=reply)  # nosec B113

    message_stub = MessageStub()
    message_stub.args = "Test User"

    await quotecunt_command.index(message_stub)
    assert message_stub.replied == expected
