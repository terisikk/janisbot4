import requests
import json

from datetime import date
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
        try:
            replytext = restaurant.parser(requests.get(restaurant.url()))
        except Exception:
            return DEFAULT_REPLY

    return replytext


def automaatio_parser(response):
    text = parse_response_text(response)

    soup = BeautifulSoup(text, features="html.parser")
    container = soup.find("div", id="pgc-41-1-0")

    weekday = get_finnish_day_name().capitalize()
    food_today = container.find("h4", text=weekday).find_next_sibling()

    return food_today.text



def galaksi_parser(response):
    jsondata = parse_response_json(response)

    food_today = ""

    for _, value in jsondata["courses"].items():
        title = value.get("title_fi", "") 
        dietcodes = value.get("dietcodes", "")

        if dietcodes != "":
            dietcodes = f" ({dietcodes})"

        food_today += title + dietcodes + '\n'

    return food_today


def parse_response_text(response):
    return response.text if hasattr(response, "text") else response


def parse_response_json(response):
    return response.json if hasattr(response, "json") else json.loads(response)


def get_finnish_day_name():
    return WEEKDAYS[date.today().weekday()]


WEEKDAYS = ["maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai"]

Restaurant = namedtuple("Restaurant", ["url", "parser"])
RESTAURANTS = {
    "automaatio": Restaurant(
        lambda: "https://www.aaltocatering.fi/automaatiotielounas/",
        automaatio_parser),
    "galaksi": Restaurant(
        lambda: "https://www.sodexo.fi/ruokalistat/output/daily_json/121/" + str(date.today()),
        galaksi_parser)
}
