from .client import StreamsbClient
from .models import FileInfo, File, LongFile, FileList
from .errors import InvalidAPIResponse

from datetime import datetime

class FileClient(StreamsbClient):

    file_base = 'file'
    info_path = 'info'
    rename_path = 'rename'
    clone_path = 'clone'
    list_path = 'list'

    def __init__(self, api_key: str):

        super().__init__(api_key)

    def info(self, file_code:str)-> list:

        params = {'file_code': file_code}
        resp = self._get(
                self._create_url(self.file_base, self.info_path),
                params = params
            )
        if resp.get('msg') == 'OK':
            infos = []
            for result in resp.get('result', []):
                infos.append(FileInfo(result))
            return infos
        else:
            raise InvalidAPIResponse('Did not get an OK response from API.', resp)

    def rename(self, filecode: str, title: str, name: str = None):

        params = {
                'file_code': filecode, 'title': title, 
                name: name if name else title
                }
        resp = self._get(
                self._create_url(self.file_base, self.rename_path),
                params = params
                )

        if resp.get('msg') == 'OK':
            if resp.get('result', '') == 'true':
                return True
            else:
                return False
        else:
            raise InvalidAPIResponse('Did not get an OK response from API.\n{resp["msg"]}')
    
    def clone(self, filecode: str):

        params = {
                'file_code': filecode
                }
        resp = self._get(
                self._create_url(self.file_base, self.clone_path),
                params = params
                )
        if resp.get('msg') == 'OK':
            return File(resp)
        else:
            raise InvalidAPIResponse('Did not get an OK response from API.\n{resp["msg"]}')

    def list(self, filter: dict)->FileList :

        params = {}
        if filter.get('title', False):
            params.update({'title':filter.get('title')})
        if filter.get('page', False):
            params.update({'page': filter.get('page')})
        if filter.get('per_page', False):
            params.update({'per_page': filter.get('per_page')})
        if filter.get('public'):
            params.update({'public': 1 if filter.get('public', False) else 0})
        if filter.get('fld_id', False):
            params.update({'fld_id': filter.get('fld_id')})
        if filter.get('created', False):
            params.update({'created': datetime.isoformat(filter.get('created'), sep = ' ')})
        if filter.get('title', False):
            params.update({'title': filter.get('title')})

        resp = self._get(
                self._create_url(self.file_base, self.list_path),
                params
                )
        if resp.get('msg') == 'OK':
            return FileList(resp)
        else:
            raise InvalidAPIResponse('Did not get an OK response from API.\n{resp["msg"]}')
