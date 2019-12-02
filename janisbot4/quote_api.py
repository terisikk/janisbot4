import requests
import json

from urllib.parse import quote as urlquote
from janisbot4.configurations import Configurations

configs = Configurations('/app/conf/janisbot.conf')

QUOTE_API_TOKEN = configs.get('quote_api_token')
QUOTE_API_URL = configs.get('quote_api_url')

head = {'Authorization': QUOTE_API_TOKEN}


def request(request_str):
    return json.loads(requests.get(f'{QUOTE_API_URL}/{request_str}', headers=head).text)


def get_random_quote(includes=None):
    req = 'random_quotes?limit=1'
    return request(req)[0].get('quote', None)


def _parse_includes(includes=None):
    parsed = [f"quote.ilike.*{urlquote(item, safe='')}*" for item in includes]
    return ','.join(parsed)
