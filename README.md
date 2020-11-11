# requests_extra

Drop-in wrapper around the [Requests](https://github.com/psf/requests) library
that provides these **extra** features:

For resiliency:
* Retry by default (3 times in total),
* Timeout by default (10 seconds),
* Exception on 4xx and 5xx responses by default (automatic `raise_for_status()`),

For performance:
* Support for Brotli enabled by default,

## Example

```
from requests_extra.api import get
get('https://httpbin.org/headers')
```

## Contributing

*ALL* kinds of issues & PRs are very welcome! There are no formal rules of contributing yet, please use common sense. ;)

## TODO

Tests.

And more features:
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
