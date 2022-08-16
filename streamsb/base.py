from .account import AccountClient
from .file import FileClient
from .folder import FolderClient

class Client:

    def __init__(self, api_key:str = None):
        self.account = AccountClient(api_key)
        self.file = FileClient(api_key)
        self.folder = FolderClient(api_key)
