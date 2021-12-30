import requests
from datetime import datetime

from bs4 import BeautifulSoup


COMMANDS = ['food']

DEFAULT_REPLY = "Ravintolasi on perseestä!"


async def index(message):
    arguments = message.get_args().split(' ')
    restaurant = RESTAURANTS.get(arguments[0], None)

    replytext = await get_food(restaurant) if restaurant else DEFAULT_REPLY

    await message.reply(replytext, reply=False)


async def get_food(restaurant):
    text = requests.get(restaurant["url"]).text
    return restaurant["filter"](text)


def get_finnish_day_name():
    weekday = datetime.today().weekday()
    return WEEKDAYS[weekday]


def automaatio_filter(text):
    try:
        soup = BeautifulSoup(text, features="html.parser")
        container = soup.find("div", id="pgc-41-1-0")
        weekday = get_finnish_day_name().capitalize()

        food_today = container.find("h4", text=weekday).find_next_sibling().text
        return food_today
    except Exception:
        return DEFAULT_REPLY


WEEKDAYS = ["maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai"]

RESTAURANTS = {
    "automaatio": {
        "url": "https://www.aaltocatering.fi/automaatiotielounas/",
        "filter": automaatio_filter
    }
}
