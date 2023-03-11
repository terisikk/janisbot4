from janisbot4.api import lorrem_api
from janisbot4.config import cfg


def test_lorrem_can_be_parsed_from_response(requests_mock):
    test_quote = "test lorr"
    response = {"lorrem": [test_quote]}
    url = cfg.get("lorrem_api_url") + "/markovpy"

    adapter = requests_mock.get(url, json=response)
    response = lorrem_api.get_random_lorr()

    assert adapter.called
    assert test_quote == response


def test_no_exception_with_empty_response(requests_mock):
    excpected = "???"
    response = {}
    url = cfg.get("lorrem_api_url") + "/markovpy"

    adapter = requests_mock.get(url, json=response)
    response = lorrem_api.get_random_lorr()

    assert adapter.called
    assert excpected == response
