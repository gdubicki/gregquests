# gregquests

This is a wrapper around the [Requests](https://github.com/psf/requests) library
that provides these extra features:

* Retry by default (3 times in total),
* Timeout by default (10 seconds),
* Exception on 4xx and 5xx responses (`raise_for_status()`) by default,
* Support for Brotli enabled by default,

It should be a drop-in replacement for requests.

## Example

```
from gregquests.api import get
get('https://httpbin.org/headers')
```

## TODO

* Single line logging of requests and/or responses, with default secrets redaction,
* HTTP/2 support (by switching to [encode/httpx](https://github.com/encode/httpx) as a backend),
* Rate limiting support, including respecting the appropriate HTTP headers,
* Support for RFC-2782 style DNS SRV entries (for Consul) -
  see [pstiasny/requests-srv](https://github.com/pstiasny/requests-srv),
* Service-to-service authentication on GCP -
  see [adrianchifor/requests-gcp](https://github.com/adrianchifor/requests-gcp),
* Built-in support for caching responses? -
  maybe with [reclosedev/requests-cache](https://github.com/reclosedev/requests-cache)
  or [bionikspoon/cache_requests](https://github.com/bionikspoon/cache_requests)

## Credits

I have copied the code for timeouts and `raise_for_status()` from
the [better-requests/better-requests](https://github.com/better-requests/better-requests) library.

I have read and reused a few concepts from
the [CarlosAMolina/requests_custom](https://github.com/CarlosAMolina/requests_custom) library.

## License

Like the upstream Requests, and the libraries I reused/was inspired with,
this library uses the Apache 2.0 license.
