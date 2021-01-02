import pytest
from requests.exceptions import ConnectionError

import requests_extra.defaults
from requests_extra import get


# import logging
# logging.basicConfig(level=logging.DEBUG)


def test_timeouts_enabled_by_default():

    requests_extra.defaults.timeout = 1
    requests_extra.defaults.retries_total = 0

    with pytest.raises(ConnectionError):
        print(get("https://httpbin.org/delay/2"))

    requests_extra.defaults.timeout = 10
    requests_extra.defaults.retries_total = 2
