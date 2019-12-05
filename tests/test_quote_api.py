import unittest
import responses

from janisbot4 import quote_api
from janisbot4.config import cfg


class TestQuoteApi(unittest.TestCase):

    def test_includes_can_be_added(self):
        includes = ["test", "test2"]
        expected = "&quote=ilike.*test*&quote=ilike.*test2*"

        includestr = quote_api._parse_arguments(includes)
        self.assertEqual(includestr, expected)

    def test_both_includes_and_excludes_can_be_added(self):
        excludes = ["test", "-test2"]
        expected = "&quote=ilike.*test*&quote=not.ilike.*test2*"

        includestr = quote_api._parse_arguments(excludes)
        self.assertEqual(includestr, expected)

    def test_includes_are_injection_safe(self):
        includes = ["test&user=root", "test2/../.htaccess"]
        includestr = quote_api._parse_arguments(includes)
        expected = f"&quote=ilike.*test%26user%3Droot*&quote=ilike.*test2%2F..%2F.htaccess*"
        self.assertEqual(includestr, expected)

    @responses.activate
    def test_quote_can_be_parsed_from_response(self):
        test_quote = 'test_quote'
        expected = {'quote': test_quote}
        url = cfg.get('quote_api_url') + '/random_quotes?limit=1'

        responses.add(responses.GET, url, json=[expected])
        response = quote_api.get_random_quote()

        self.assertEqual(test_quote, response)

    @responses.activate
    def test_no_exception_with_empty_response(self):
        excpected = '???'
        url = cfg.get('quote_api_url') + '/random_quotes?limit=1'

        responses.add(responses.GET, url, json=[{}])
        response = quote_api.get_random_quote()

        self.assertEqual(excpected, response)
