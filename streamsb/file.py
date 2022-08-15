from .client import StreamsbClient
from .models import (FileInfo, File, 
        LongFile, FileList, Quality)
from .errors import InvalidAPIResponse

from datetime import datetime

class FileClient(StreamsbClient):

    file_base = 'file'
    info_path = 'info'
    rename_path = 'rename'
    clone_path = 'clone'
    list_path = 'list'
    direct_all_path = 'direct'
    direct_url_path = 'direct_link'
    set_folder_path = 'set_folder'

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
            raise InvalidAPIResponse(f'Did not get an OK response from API.', resp)

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
            raise InvalidAPIResponse(f'Did not get an OK response from API.\n{resp["msg"]}')
    
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
            raise InvalidAPIResponse(f'Did not get an OK response from API.\n{resp["msg"]}')

    def list(self, filter: dict = {})->FileList :

        params = {}
        if filter.get('title', False):
            params.update({'title':filter.get('title')})
        if filter.get('page', False):
            params.update({'page': filter.get('page')})
        if filter.get('per_page', False):
            params.update({'per_page': filter.get('per_page')})
        if filter.get('public'):
            params.update({'public': 1 if filter.get('public', False) else 0})
        if filter.get('folder_id', False):
            params.update({'fld_id': filter.get('fld_id')})
        if filter.get('created', False):
            try:
                params.update({'created': datetime.isoformat(filter.get('created'), sep = ' ')})
            except:
                print('filter.created must be a datetime object')
                pass
        if filter.get('title', False):
            params.update({'title': filter.get('title')})

        resp = self._get(
                self._create_url(self.file_base, self.list_path),
                params
                )
        if resp.get('msg') == 'OK':
            return FileList(resp)
        else:
            raise InvalidAPIResponse(f'Did not get an OK response from API.\n{resp["msg"]}')

    def direct_all(self, filecode: dict) ->dict :

        params = {'file_code': filecode}
        resp = self._get(
                self._create_url(self.file_base, self.direct_all_path),
                params
                )
        if resp.get('msg') == 'OK':
            qualities = {}
            for k,v in resp.get('result', {}).items():
                qualities[k] = Quality(v)
            return qualities
        else:
            raise InvalidAPIResponse(f'Did not get an OK response from API.\n{resp["msg"]}')

    def direct_url(self, filecode: str, quality: str) -> Quality:

        params = {'file_code': filecode, 'q': quality}
        resp = self._get(
                self._create_url(self.file_base, self.direct_url_path),
                params
                )
        if resp.get('msg') == 'OK':
            quality = Quality()
            q.url = resp.get('url', None)
            q.size = int(resp.get('size', 0))
            return quality
        else:
            raise InvalidAPIResponse(f'Did not get an OK response from API.\n{resp["msg"]}')

    def set_folder(self, filecode: str, folder_id: str) -> bool :

        params = {'file_code': filecode, 'fld_id': folder_id}
        resp = self._get(
                self._create_url(self.file_base, self.set_folder_path),
                params
                )
        if resp.get('msg') == 'OK':
            return True
        else:
            raise InvalidAPIResponse(f'Did not get an OK response from API.\n{resp["msg"]}')
