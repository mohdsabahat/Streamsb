class Account:

    def __init__(self, resp):

        self.raw = resp
        self._deserialize(resp['result'])

    def _deserialize(self, result:dict):

        for k,v in result.items():
            setattr(self, k, v)

class Stat(Account):

    def __init__(self, data:dict):
        self.raw = data
        super()._deserialize(data)

class AccountInfo(Account):

    def __init__(self, resp):
        super().__init__(resp)

class AccountStat(Account):

    def __init__(self, resp):
        self.raw = resp
        self.stat = []
        for r in self.raw['result']:
            self.stat.append(Stat(r))
