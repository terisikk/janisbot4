import requests

from datetime import datetime
from collections import namedtuple
from bs4 import BeautifulSoup


COMMANDS = ['food']

DEFAULT_REPLY = "Ravintolasi on perseestä!"


async def index(message):
    arguments = message.get_args().strip()
    replytext = DEFAULT_REPLY

    if arguments != "":
        replytext = await get_food(arguments)

    await message.reply(replytext, reply=False)


async def get_food(restaurant_name):
    restaurant = RESTAURANTS.get(restaurant_name, None)
    replytext = DEFAULT_REPLY

    if restaurant:
        replytext = restaurant.parser(requests.get(restaurant.url))

    return replytext


def automaatio_parser(response):
    text = parse_response(response)

    try:
        soup = BeautifulSoup(text, features="html.parser")
        container = soup.find("div", id="pgc-41-1-0")

        weekday = get_finnish_day_name().capitalize()
        food_today = container.find("h4", text=weekday).find_next_sibling()

        return food_today.text
    except Exception:
        return DEFAULT_REPLY


def parse_response(response):
    return response.text if hasattr(response, "text") else response


def get_finnish_day_name():
    return WEEKDAYS[datetime.today().weekday()]


WEEKDAYS = ["maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai"]

Restaurant = namedtuple("Restaurant", ["url", "parser"])
RESTAURANTS = {
    "automaatio": Restaurant(
        "https://www.aaltocatering.fi/automaatiotielounas/",
        automaatio_parser)
}
