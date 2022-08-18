from .client import StreamsbClient
from .errors import InvalidAPIResponse
from .models import LongFile
from .models import FolderList

class FolderClient(StreamsbClient):

    folder_base = 'folder'
    list_path = 'list'
    create_path = 'create'

    def __init__(self, api_key: str):

        super().__init__(api_key)

    def list(self, folder_id: str = None):

        params = {}
        if folder_id:
            params.update({'fld_id': folder_id})
        resp = self._get(
                self._create_url(self.folder_base, self.list_path),
                params
                )
        result = {}
        if resp.get('msg') == 'OK':
            res = resp.get('result', {})
            result['raw'] = resp
            result['folders'] = FolderList(res.get('folders', []))
            result['files'] = []
            for file in res.get('files', []):
                result['files'].append(LongFile(file))
            return result
        else:
            raise InvalidAPIResponse(f'Did not get an OK response from API.\n{resp["msg"]}')

    def create(self, name: str, parent_id: int = None):

        params = {}
        params.update({'name': name})
        if parent_id:
            params.update({'fld_id': parent_id})
        resp = self._get(
                self._create_url(self.folder_base, self.create_path),
                params
                )
        if resp.get('msg') == 'OK':
            return resp.get('result',{}).get('fld_id', None)
        else:
            raise InvalidAPIResponse(f'Did not get an OK response from API.\n{resp["msg"]}')
