import pytest
from requests.exceptions import HTTPError

import requests_extra.defaults
from requests_extra import get


def test_exception_on_4xx():

    requests_extra.defaults.retries_total = 0

    with pytest.raises(HTTPError):
        print(get("https://httpbin.org/status/400"))

    requests_extra.defaults.retries_total = 2


def test_exception_on_5xx():

    requests_extra.defaults.retries_total = 0

    with pytest.raises(HTTPError):
        # let's use one of the code that DO NOT trigger autoretry
        # - otherwise this will be much longer
        print(get("https://httpbin.org/status/501"))

    requests_extra.defaults.retries_total = 2
