import requests
import json

from configurations import Configurations

configs = Configurations('/app/conf/janisbot.conf')

QUOTE_API_TOKEN = configs.get('quote_api_token')
QUOTE_API_URL = configs.get('quote_api_url')

head = {'Authorization': QUOTE_API_TOKEN}


def get_random_quote():
    return json.loads(requests.get(f'{QUOTE_API_URL}/random_quotes?limit=1', headers=head).text)[0].get('quote', None)
