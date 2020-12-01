import pytest
from requests.exceptions import RetryError

from requests_extra.api import get


def test_retries_enabled_by_default():

    with pytest.raises(RetryError):
        print(get("https://httpbin.org/status/429"))
