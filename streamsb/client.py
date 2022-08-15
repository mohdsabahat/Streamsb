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

    def _get(self, url:str, params:dict = {}):

        print('api : ', self.api_key)
        print('url :', url)
        params.update({'key': self.api_key})
        try:
            resp = requests.get(url, params = params)
            print(resp.headers)
        except Exception as e:
            raise APIError(0, e)

        code = resp.status_code
        if resp.ok:
            return resp.json()
        elif code>=400 or code<500:
            if code == 404:
                raise NotFound(self.api_key)
            elif code == 403:
                raise AccountNotFound(self.api_key, resp.json()['msg'])
            else:
                raise APIError(code)
        elif code>=500:
            raise APIError(code)
        else:
            return {}
