import pytest

import janisbot4.plugins.food_command as food


@pytest.mark.asyncio
async def test_randchoice(conv):
    options = ["test1", "test2"]

    await conv.send_message("/randchoice " + " ".join(options))

    response = await conv.get_response()

    assert response is not None
    assert response.raw_text in options


@pytest.mark.asyncio
async def test_quote(conv):
    await conv.send_message("/quote rotta")
    response = await conv.get_response()

    assert response is not None
    assert "rotta" in response.raw_text.lower()


@pytest.mark.asyncio
async def test_food(conv):
    await conv.send_message("/food galaksi")
    response = await conv.get_response()

    assert response is not None
    assert response.raw_text != ""
    assert response.raw_text != food.DEFAULT_REPLY


@pytest.mark.asyncio
async def test_lorr(conv):
    await conv.send_message("/lorr test")
    response = await conv.get_response()

    assert response is not None
    assert response.raw_text != ""


@pytest.mark.asyncio
async def test_blame(conv):
    await conv.send_message("/quote rotta")
    message = await conv.get_response()
    await message.reply("/blame")
    response = await conv.get_response()

    assert response is not None
    assert response.raw_text != ""


@pytest.mark.asyncio
async def test_quotecunt(conv):
    await conv.send_message("/quotecunt")
    response = await conv.get_response()

    assert response is not None
    assert response.raw_text != ""
    assert response.raw_text.isnumeric()


@pytest.mark.asyncio
async def test_quote_message(conv):
    await conv.send_message("test:")
    response = await conv.get_response()

    assert response is not None
    assert response.raw_text != ""
