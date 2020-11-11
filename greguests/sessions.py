import requests.sessions as upstream_session
from requests.adapters import HTTPAdapter
from urllib3 import Retry


class Session(upstream_session.Session):
    """A Requests session.

        + retries.
    """

    def __init__(self):
        super(Session, self).__init__()

        retries: Retry = Retry(
            total=2,  # 3 requests in total
            backoff_factor=1,  # retry after 2, 4 secs
            status_forcelist=[500, 502, 503, 504, 429],  # on server errors + rate limit exceeded
            method_whitelist=[
                "HEAD",
                "GET",
                "PUT",
                "POST",  # DO retry for POSTs
                "DELETE",
                "OPTIONS",
                "TRACE",
            ],
        )
        self.mount("http://", HTTPAdapter(max_retries=retries))
        self.mount("https://", HTTPAdapter(max_retries=retries))


