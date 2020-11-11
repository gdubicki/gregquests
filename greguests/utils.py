from requests.structures import CaseInsensitiveDict
from requests.utils import default_user_agent


def default_headers_with_brotli():
    """
    :rtype: requests.structures.CaseInsensitiveDict
    """
    return CaseInsensitiveDict({
        'User-Agent': default_user_agent(),
        'Accept-Encoding': ', '.join(('br', 'gzip', 'deflate')),
        'Accept': '*/*',
        'Connection': 'keep-alive',
    })
