#!/usr/bin/env python3

from greguests.sessions import Session

import http
http.client.HTTPConnection.debuglevel = 1

x = Session()
x.get('https://httpbin.org/status/429')
