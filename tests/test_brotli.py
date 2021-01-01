from requests_extra import get


def test_brotli_enabled_by_default():
    response = get("https://httpbin.org/headers")
    assert 'br' in response.request.headers['accept-encoding']
