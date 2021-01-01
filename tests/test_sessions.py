from requests_extra import get


import logging
logging.basicConfig(level=logging.DEBUG)


def test_sessions_automatically_reused_for_same_scheme_and_netloc(caplog):

    # we will capture the debug logs that will print sth like "Got session from cache"
    caplog.set_level(logging.DEBUG)

    get("https://httpbin.org/ip")
    get("https://httpbin.org/user-agent")

    second_request_reused_session = False
    for record in caplog.records:
        if "Got session from cache!" in record.getMessage():
            second_request_reused_session = True
            break

    assert second_request_reused_session


def test_automatic_session_cookies_working_on_first_request():

    # on the 1st request that gets a response with cookies we SHOULD be able to read them
    response1 = get("https://httpbin.org/cookies/set/foo/bar", allow_redirects=False)
    assert response1.cookies['foo'] == 'bar'


def test_automatic_session_cookies_not_getting_passed_on_subsequent_requests():

    # on the 1st request that gets a response with cookies we SHOULD be able to read them

    response1 = get("https://httpbin.org/cookies/set/foo2/bar2", allow_redirects=False)
    assert response1.cookies['foo2'] == 'bar2'

    # ...but the 2nd request should NOT contain the cookie set above!

    response2 = get("https://httpbin.org/cookies")
    assert response2.json()['cookies'] == {}
