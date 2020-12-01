import pytest

from requests_extra.api import get
from requests.exceptions import ConnectionError


def test_sessions_automatically_created():

    response1 = get("https://httpbin.org/ip")
    response2 = get("https://httpbin.org/user-agent")

    # TODO: how to check if it's the same session? :pointup

    assert True
