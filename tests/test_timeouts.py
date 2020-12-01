import pytest

from requests_extra.api import get
from requests.exceptions import ConnectionError


def test_timeouts_enabled_by_default():

    with pytest.raises(ConnectionError):
        print(get("https://httpbin.org/delay/15"))
