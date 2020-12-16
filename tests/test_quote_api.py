from janisbot4 import quote_api
from janisbot4.config import cfg


def test_includes_can_be_added():
    includes = ["test", "test2"]
    expected = "&quote=ilike.*test*&quote=ilike.*test2*"

    includestr = quote_api._parse_arguments(includes)
    assert includestr == expected


def test_both_includes_and_excludes_can_be_added():
    excludes = ["test", "-test2"]
    expected = "&quote=ilike.*test*&quote=not.ilike.*test2*"

    includestr = quote_api._parse_arguments(excludes)
    assert includestr == expected


def test_includes_are_injection_safe():
    includes = ["test&user=root", "test2/../.htaccess"]
    includestr = quote_api._parse_arguments(includes)
    expected = "&quote=ilike.*test%26user%3Droot*&quote=ilike.*test2%2F..%2F.htaccess*"
    assert includestr == expected


def test_quote_can_be_parsed_from_response(requests_mock):
    test_quote = 'test_quote'
    response = [{'quote': test_quote}]
    url = cfg.get('quote_api_url') + '/random_quotes?limit=1'

    requests_mock.get(url, json=response)
    response = quote_api.get_random_quote()

    assert test_quote == response


def test_no_exception_with_empty_response(requests_mock):
    excpected = '???'
    response = [{}]
    url = cfg.get('quote_api_url') + '/random_quotes?limit=1'

    requests_mock.get(url, json=response)
    response = quote_api.get_random_quote()

    assert excpected == response
