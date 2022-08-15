from .client import StreamsbClient
from .models import FileInfo, File, LongFile
from .errors import InvalidAPIResponse

class FileClient(StreamsbClient):

    file_base = 'file'
    info_path = 'info'
    rename_path = 'rename'
    clone_path = 'clone'

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
