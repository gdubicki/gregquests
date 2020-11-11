#!/usr/bin/env python3

from requests.exceptions import RetryError, ConnectionError
from gregquests.api import get

import http

http.client.HTTPConnection.debuglevel = 1

print("Example 1: brotli support")

get("https://httpbin.org/headers")

print("Example 2: default retries")

try:
    get("https://httpbin.org/status/429")
except RetryError:
    print("Max retries reached, as expected.")

print("Example 3: default timeout + retries")

try:
    get("https://httpbin.org/delay/15")
except ConnectionError:
    print("Max retries after timeouts reaches, as expected.")
