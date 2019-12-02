import unittest

from janisbot4 import quote_api


class TestQuoteApi(unittest.TestCase):

    def test_includes_can_be_added(self):
        includes = ["test", "test2"]
        expected = "quote.ilike.*test*,quote.ilike.*test2*"

        includestr = quote_api._parse_includes(includes)
        self.assertEqual(includestr, expected)

    def test_includes_are_injection_safe(self):
        includes = ["test&user=root", "test2/../.htaccess"]
        includestr = quote_api._parse_includes(includes)
        expected = f"quote.ilike.*test%26user%3Droot*,quote.ilike.*test2%2F..%2F.htaccess*"

        self.assertNotIn("&", includestr)
        self.assertNotIn("=", includestr)
        self.assertNotIn("/", includestr)

        self.assertEqual(includestr, expected)
