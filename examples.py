#!/usr/bin/env python3

from requests.exceptions import RetryError, ConnectionError
from requests_extra.api import get
import logging



print("*** Example 1: brotli support ***")

response = get("http://httpbin.org/headers")
print(response.request.headers)



print("*** Example 2: automatic reusing HTTP connections support ***")

print("Enabling debug logging to show this.")
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

print("   Making 1st connection to httpbin.org over HTTPS:")
response = get("https://httpbin.org/cookies/set/foo/bar")
print("   Note that we are NOT storing the cookies to emulate non-session behavior for a drop-in replacement!")
print(response.cookies)

print("   Making 2nd connection to httpbin.org over HTTPS:")
response = get("https://httpbin.org/cookies/set/what/ever")
print(response.cookies)

logging.disable(logging.DEBUG)



print("*** Example 3: default retries ***")

try:
    print(get("https://httpbin.org/status/429"))
except RetryError:
    print("Max retries reached, as expected.")

print("*** Example 4: default timeout + retries ***")

try:
    print(get("https://httpbin.org/delay/15"))
except ConnectionError:
    print("Max retries after timeouts reaches, as expected.")
