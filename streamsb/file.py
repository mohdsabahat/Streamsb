from .client import StreamsbClient

class FileClient(StreamsbClient):

    def __init__(self, api_key):

        super().__init__(api_key)
