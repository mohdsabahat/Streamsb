
class StreamsbError(Exception):

    def __str__(self):
        return 'An Error occured'


class APIError(StreamsbError):

    def __init__(self, code, msg=None):
        self.code = code
        self.msg = msg

    def __str__(self):

        return f'{self.code}: {self.msg}'

class InvalidAPIResponse(StreamsbError):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):

        return f'{self.msg}'

class NotFound(StreamsbError):

    def __init__(self, code, msg = ''):
        self.code = code
        self.message = msg

    def __str__(self):
        if self.message:
            return f'{self.message} : {self.code}'
        return f'Resource Not Found : {self.code}'

class AccountNotFound(StreamsbError):

    def __init__(self, code, msg):

        self.code = code
        self.msg = msg

    def __str__(self):

        return f'Account not found with API Key :{self.code}\nCheck if the key is correct!\nAPI Response : {self.msg}'
