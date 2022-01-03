import pytest
from datetime import date

from janisbot4.plugins import food_command

from unittest.mock import patch
from tests.message_stub import MessageStub


@pytest.mark.asyncio
async def test_automaatio_list_is_returned_on_command(requests_mock):
    with patch('janisbot4.plugins.food_command.date') as mock_date:
        mock_date.today.return_value = date(2021, 12, 28)
        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)

        url = "https://www.aaltocatering.fi/automaatiotielounas/"

        requests_mock.get(url, text=TEST_DATA_AUTOMAATIO)

        message = MessageStub()
        message.args = "automaatio"

        await food_command.index(message)

        assert food_command.date.today() == date(2021, 12, 28)
        assert message.replied != food_command.DEFAULT_REPLY


@pytest.mark.asyncio
async def test_galaksi_list_is_returned_on_command(requests_mock):
    with patch('janisbot4.plugins.food_command.date') as mock_date:
        mock_date.today.return_value = date(2021, 12, 28)
        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)

        url = "https://www.sodexo.fi/ruokalistat/output/daily_json/121/" + str(mock_date.today())

        requests_mock.get(url, text=TEST_DATA_GALAKSI)

        message = MessageStub()
        message.args = "galaksi"

        await food_command.index(message)
        assert message.replied != food_command.DEFAULT_REPLY


@pytest.mark.parametrize("restaurant", ["nonexisting", ""])
@pytest.mark.asyncio
async def test_default_reply_on_nonexisting_restaurant(requests_mock, restaurant):
    message = MessageStub()
    message.args = restaurant

    await food_command.index(message)
    assert message.replied == food_command.DEFAULT_REPLY


@pytest.mark.asyncio
async def test_default_reply_on_faulty_content(requests_mock):
    url = "https://www.aaltocatering.fi/automaatiotielounas/"

    requests_mock.get(url, text="empty data")

    replytext = await food_command.get_food("automaatio")

    assert replytext == food_command.DEFAULT_REPLY


def test_automaatio_restaurant_list_can_be_parsed():
    with patch('janisbot4.plugins.food_command.date') as mock_date:
        mock_date.today.return_value = date(2021, 12, 28)
        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)

        expected = """\
Test food 2
Test food 3
"""

        food = food_command.automaatio_parser(TEST_DATA_AUTOMAATIO)
        assert food == expected


def test_galaksi_restaurant_list_can_be_parsed():
    expected = """\
Test food 1 (M, G)
Test food 2
"""

    food = food_command.galaksi_parser(TEST_DATA_GALAKSI)
    assert food == expected


TEST_DATA_AUTOMAATIO = """\
<div id="pgc-41-1-0" class="panel-grid-cell">
<div id="panel-41-1-0-0" class="so-panel widget widget_text panel-first-child panel-last-child" data-index="1">
<div class="flash_inherit_color panel-widget-style panel-widget-style-for-41-1-0-0">
<h3 class="widget-title">20.12-22.12.2021</h3>
<div class="textwidget">
<h4>Maanantai</h4>
<p>Test food 1/p>
<h4>Tiistai</h4>
<p>Test food 2<br>
Test food 3<br>
</p>
</div>
</div>
</div>
</div>
"""

TEST_DATA_GALAKSI = """
{
    "courses": {
        "1": {
            "title_fi": "Test food 1",
            "dietcodes": "M, G"
        },
        "2": {
            "title_fi": "Test food 2"
        }
    }
}
"""
