import pytest
from datetime import date

from janisbot4.plugins import food_command

from unittest.mock import patch
from tests.message_stub import MessageStub


@pytest.mark.asyncio
async def test_food_list_is_returned_on_command(requests_mock):
    with patch('janisbot4.plugins.food_command.datetime') as mock_date:
        mock_date.today.return_value = date(2021, 12, 28)
        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)

        url = "https://www.aaltocatering.fi/automaatiotielounas/"

        requests_mock.get(url, text=TEST_DATA)

        message = MessageStub()
        message.args = "automaatio"

        await food_command.index(message)

        assert food_command.datetime.today() == date(2021, 12, 28)
        assert message.replied != food_command.DEFAULT_REPLY


@pytest.mark.parametrize("restaurant", ["nonexisting", ""])
@pytest.mark.asyncio
async def test_default_reply_on_nonexisting_restaurant(requests_mock, restaurant):
    message = MessageStub()
    message.args = restaurant

    await food_command.index(message)
    assert message.replied == food_command.DEFAULT_REPLY


def test_default_reply_on_faulty_automaatio_content(requests_mock):
    reply = food_command.automaatio_parser("empty text")
    assert reply == food_command.DEFAULT_REPLY


def test_automaatio_restaurant_list_can_be_parsed():
    with patch('janisbot4.plugins.food_command.datetime') as mock_date:
        mock_date.today.return_value = date(2021, 12, 28)
        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)

        expected = """\
Sweet chili broileria ja nuudeleita M L,G
Kokonaisena paistettua porsaansisäfilettä M,G (*Suomi)
Bouillabaisse M,G
Pizzabuffet
Päivän kasvisruoka tilataan keittiöstä:
Punajuuri-aurajuustovuoka L,G"""

        food = food_command.automaatio_parser(TEST_DATA)
        assert food == expected


TEST_DATA = """
<div id="pgc-41-1-0" class="panel-grid-cell">
<div id="panel-41-1-0-0" class="so-panel widget widget_text panel-first-child panel-last-child" data-index="1">
<div class="flash_inherit_color panel-widget-style panel-widget-style-for-41-1-0-0">
<h3 class="widget-title">20.12-22.12.2021</h3>
<div class="textwidget">
<p>Lounas tarjolla klo 10.30-13.00<br>
Tervetuloa!</p>
<h4>Maanantai</h4>
<p>Kermainen lihapata L,G<br>
Paistettua kalaa L,G<br>
Tomaatti-vuohenjuustokeittoa VL,G<br>
Pizzabuffet<br>
Päivän kasvisruoka tilataan keittiöstä:<br>
Kasviskaalikääryleitä M,G</p>
<h4>Tiistai</h4>
<p>Sweet chili broileria ja nuudeleita M L,G<br>
Kokonaisena paistettua porsaansisäfilettä M,G (*Suomi)<br>
Bouillabaisse M,G<br>
Pizzabuffet<br>
Päivän kasvisruoka tilataan keittiöstä:<br>
Punajuuri-aurajuustovuoka L,G</p>
<h4>Keskiviikko</h4>
<p>Grillikylkeä M,G<br>
Häränfilehöystöä L.G<br>
Aurajuusto-kukkakaalikeittoa L,G (*Suomi)<br>
Pizzabuffet<br>
Päivän kasvisruoka tilataan keittiöstä:<br>
Kasviscurrya M,G</p>
</div>
</div>
</div>
</div>
"""
