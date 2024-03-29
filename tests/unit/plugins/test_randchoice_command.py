import pytest

from janisbot4.plugins import randchoice_command
from tests.unit.message_stub import MessageStub


@pytest.mark.asyncio
async def test_random_choice_is_returned_on_command():
    expected = ["choice1", "choice2", "choice3"]

    message_stub = MessageStub()
    message_stub.args = "choice1 choice2 choice3"

    await randchoice_command.index(message_stub)
    assert message_stub.replied in expected


@pytest.mark.asyncio
async def test_randchoice_does_not_split_phrases():
    expected = "This is the choice"

    message_stub = MessageStub()
    message_stub.args = "'This is the choice'"

    await randchoice_command.index(message_stub)
    assert message_stub.replied in expected
