from .client import StreamsbClient
from .errors import InvalidAPIResponse
import os

class UploadClient(StreamsbClient):

    upload_base = 'upload'
    server_path = 'server'
    url_path = 'url'

    def __init__(self, api_key: str):

        super().__init__(api_key)

    def get_server(self) -> str:

        params = {}
        resp = self._get(
                self._create_url(self.upload_base, self.server_path),
                params
                )
        if resp.get('msg') == 'OK':
            return resp.get('result')
        else:
            raise InvalidAPIResponse(f'Did not get an OK response from API.\n{resp["msg"]}')

    def file(self, upload_url: str, file_path: str):

        # Upload Not working
        if not os.path.exists(file_path):
            return NotFound(404, 'File does not exists! Please recheck.')
        params = {}
        resp = self._post(
                upload_url,
                params
                )

    def url(self, upload_url: str) -> str:

        params = {'url': upload_url}
        resp = self._get(
                self._create_url(self.upload_base, self.url_path),
                params
                )
        if resp.get('msg') == 'OK':
            return resp.get('result',{}).get('filecode', None)
        else:
            raise InvalidAPIResponse(f'Did not get an OK response from API.\n{resp["msg"]}')

