from .client import StreamsbClient
from .errors import InvalidAPIResponse, AccountNotFound, NotFound
from .session import APISession
from .models import AccountInfo, AccountStat

class AccountClient(StreamsbClient):

    account_base = 'account/'
    info_path = 'info'
    stat_path = 'stats'

    def __init__(self, api_key: str):

        super().__init__(api_key)

    def info(self):

        resp = self._get(
                self._create_url(self.account_base, self.info_path),
                )

        if resp.get('msg') == 'OK':
            return AccountInfo(resp)
        else:
            raise InvalidAPIResponse('Did not get an OK response from API.', resp)

    def stats(self):

        resp = self._get(
                self._create_url(self.account_base, self.stat_path)
                )
        if resp.get('msg') == 'OK':
            return AccountStat(resp)
        else:
            raise InvalidAPIResponse(f'Did not get an OK response from API.{resp["msg"]}')
