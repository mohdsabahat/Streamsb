
class Folder:

    def __init__(self, resp: dict):

        self.raw = resp
        self.name = resp.get('name', None)
        self.folder_id = resp.get('fld_id', None)
        self.code = resp.get('code', None)

class FolderList:

    def __init__(self, resp: list):

        self.raw = resp
        self.folders = []
        for folder in resp:
            self.folders.append(Folder(folder))
