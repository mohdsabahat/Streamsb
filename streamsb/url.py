from .client import StreamsbClient
from .errors import InvalidAPIResponse

class UrlClient(StreamsbClient):

    url_base = 'url'
    add_path = ''
