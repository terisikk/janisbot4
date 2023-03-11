import pytest
import janisbot4.plugins.lorr_command as lorr_command

from janisbot4.config import cfg
from tests.message_stub import MessageStub


@pytest.mark.asyncio
async def test_lorr_is_returned_on_command(requests_mock):
    expected = "test lorr"
    reply = {"lorrem": [expected]}
    url = cfg.get("lorrem_api_url") + "/markovpy"

    requests_mock.get(url, json=reply)

    message_stub = MessageStub()

    await lorr_command.index(message_stub)
    assert message_stub.replied == expected
