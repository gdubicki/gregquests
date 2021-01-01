import pytest
from requests.exceptions import RetryError

from requests_extra import get

import logging
logging.basicConfig(level=logging.DEBUG)


def test_retries_enabled_by_default():

    # this should fail as each retry will always get HTTP 429
    with pytest.raises(RetryError):
        print(get("https://httpbin.org/status/429"))
