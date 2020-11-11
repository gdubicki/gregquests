#!/usr/bin/env python3
import sys

from requests.exceptions import RetryError, ConnectionError
from greguests.sessions import Session

import http
http.client.HTTPConnection.debuglevel = 1

x = Session()



print("Example 1: brotli support")

x.get('https://httpbin.org/headers')



print("Example 2: default retries")

try:
    x.get('https://httpbin.org/status/429')
except RetryError:
    print("Max retries reached, as expected.")



print("Example 3: default timeout + retries")

try:
    x.get('https://httpbin.org/delay/15')
except ConnectionError:
    print("Max retries after timeouts reaches, as expected.")
