#!/usr/bin/env python3

from requests.exceptions import RetryError, ConnectionError
from requests_extra.api import get
from requests_extra.api import get_session

import http
# http.client.HTTPConnection.debuglevel = 1

print("Example 1: brotli support")

print(get("https://httpbin.org/headers"))

print("Example 2: automatic reusing HTTP connections support")

print(get("https://httpbin.org/cookies/set/foo/bar"))

print("Automatic sessions DO NOT store cookies to simulate non-session requests")
print(get("https://httpbin.org/cookies"))

print(get_session.cache_info())

print("Example 3: default retries")

try:
    print(get("https://httpbin.org/status/429"))
except RetryError:
    print("Max retries reached, as expected.")

print("Example 4: default timeout + retries")

try:
    print(get("https://httpbin.org/delay/15"))
except ConnectionError:
    print("Max retries after timeouts reaches, as expected.")

print(get_session.cache_info())
