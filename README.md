This is a set of wrappers around the ubiquitous Requests library that provide extensions that I find necessary
for most uses:

* Retry by default,

TODO:

* Timeout by default,
* Support for Brotli enabled by default,

Maybe:

* Caching GET responses by default,
* Support for RFC-2782 style DNS SRV entries (for Consul),
* Printing request and response with default secrets redaction, multi or single line,
