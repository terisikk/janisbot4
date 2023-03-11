import re

from janisbot4.api import quote_api
from janisbot4.config import cfg


def test_includes_can_be_added():
    includes = ["test", "test2"]
    expected = "&quote=ilike.*test*&quote=ilike.*test2*"

    includestr = quote_api._parse_include_exclude(includes)
    assert includestr == expected


def test_both_includes_and_excludes_can_be_added():
    excludes = ["test", "-test2"]
    expected = "&quote=ilike.*test*&quote=not.ilike.*test2*"

    includestr = quote_api._parse_include_exclude(excludes)
    assert includestr == expected


def test_includes_are_injection_safe():
    includes = ["test&user=root", "test2/../.htaccess"]
    includestr = quote_api._parse_include_exclude(includes)
    expected = "&quote=ilike.*test%26user%3Droot*&quote=ilike.*test2%2F..%2F.htaccess*"
    assert includestr == expected


def test_quote_can_be_parsed_from_response(requests_mock):
    test_quote = "test_quote"
    response = [{"quote": test_quote}]
    url = cfg.get("quote_api_url") + "/random_quotes?limit=1"

    adapter = requests_mock.get(url, json=response)
    response = quote_api.get_random_quote()

    assert adapter.called
    assert test_quote == response


def test_no_exception_with_empty_response(requests_mock):
    excpected = "???"
    response = [{}]
    url = cfg.get("quote_api_url") + "/random_quotes?limit=1"

    adapter = requests_mock.get(url, json=response)
    response = quote_api.get_random_quote()

    assert adapter.called
    assert excpected == response


def test_quotelast_can_be_called(requests_mock):
    url = cfg.get("quote_api_url") + "/rpc/quotelast"

    adapter = requests_mock.post(url)
    quote_api.quotelast("test_channel", "test quote", "test_victim", "test_adder")

    assert adapter.called
    assert adapter.last_request.json() == {
        "a_adder": "test_adder",
        "a_channel": "test_channel",
        "a_quote": "test quote",
        "a_victim": "test_victim",
    }


def test_quote_user_can_be_parsed_from_response(requests_mock):
    test_quote = "test_quote"
    response = [
        {"timestamp": "2012-04-14T01:46:07", "user": {"name": "Test User"}, "adder": None, "channel": {"name": "#test"}}
    ]

    url = re.compile(cfg.get("quote_api_url") + "/irc_quote.*")

    adapter = requests_mock.get(url, json=response)
    response = quote_api.get_quote_metadata(test_quote)

    assert adapter.called
    assert "Test User" == response["user"]["name"]
