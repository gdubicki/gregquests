# grequests

This is a wrapper around the [Requests](https://github.com/psf/requests) library
that provides these extra features:

* Retry by default (3 times in total),
* Timeout by default (10 seconds),
* Exception on 4xx and 5xx responses (`raise_for_status()`) by default,
* Support for Brotli enabled by default,

Maybe TODO:

* Caching GET responses by default,
* Support for RFC-2782 style DNS SRV entries (for Consul),
* Printing request and response with default secrets redaction, multi or single line,

# Credits

I have reused the code for timeouts and `raise_for_status()` from
the [better-requests](https://github.com/better-requests/better-requests) library.
