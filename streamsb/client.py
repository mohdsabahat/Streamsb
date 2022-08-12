from .session import APISession
#from .file import FileClient
#from .folder import FolderClient
#from .upload import UploadClient
from urllib.parse import urljoin
from .errors import APIError, NotFound
import requests

class StreamsbClient():

    base_url = 'https://api.streamsb.com/'
    api_base = 'api/'
    api_url = urljoin(base_url, api_base)
    api_key = None
    session = APISession()
    print('session created')

    def __init__(self, api_key: str):

        self.api_key = api_key

    def _create_url(self, *args):

        return urljoin(self.api_url, '/'.join(args))

    def _get(self, url:str):

        print('api : ', self.api_key)
        print('url :', url)
        params = {'key': self.api_key}
        try:
            resp = requests.get(url, params = params)
            print(resp.headers)
        except Exception as e:
            raise APIError(0, e.message)

        if resp.ok:
            return resp.json()
        elif resp.status_code>=400 or resp.status_code<500:
            if resp.status_code == 404:
                raise NotFound(self.api_key)
            else:
                raise APIError(resp.status_code)
        elif resp.status_code>=500:
            raise APIError(resp.status_code)
        else:
            return {}
