import requests
import json

from urllib.parse import quote as urlquote
from janisbot4.config import cfg

QUOTE_API_TOKEN = cfg.get('quote_api_token')
QUOTE_API_URL = cfg.get('quote_api_url')

head = {'Authorization': QUOTE_API_TOKEN}

EMPTY_RESPONSE = '???'


def request(request_str):
    response = requests.get(f'{QUOTE_API_URL}/{request_str}', headers=head)
    return json.loads(response.text)


def get_random_quote(arguments=None):
    req = 'random_quotes?limit=1' + _parse_arguments(arguments)
    response = request(req)
    return response[0].get('quote', EMPTY_RESPONSE) if len(response) > 0 else EMPTY_RESPONSE


def _parse_arguments(arguments=None):
    if not arguments:
        return ''

    return '&' + '&'.join([_parse_argument(arg) for arg in arguments])


def _parse_argument(argument):
    if argument.startswith('-'):
        return f"quote=not.ilike.*{urlquote(argument.lstrip('-'), safe='')}*"

    return f"quote=ilike.*{urlquote(argument, safe='')}*"
