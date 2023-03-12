import requests

from janisbot4.config import cfg


LORREM_API_URL = cfg.get("lorrem_api_url")
LORREM_API_TOKEN = cfg.get("lorrem_api_token")

EMPTY_RESPONSE = "???"

HEADERS = {"Authorization": LORREM_API_TOKEN}
REQUEST_TIMEOUT = 10


def request(request_str):
    response = requests.get(f"{LORREM_API_URL}/{request_str}", headers=HEADERS, timeout=REQUEST_TIMEOUT)
    return response.json()


def get_random_lorr():
    req = "markovpy"
    response = request(req)
    return response.get("lorrem", EMPTY_RESPONSE)[0] if len(response) > 0 else EMPTY_RESPONSE
