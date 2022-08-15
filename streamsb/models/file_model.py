from datetime import datetime

class File:

    def __init__(self, resp):

        self.raw = resp
        result = res.get('result', {})
        # API is inconsistent with file code 
        # Noticed variations = ['file_code', 'filecode']
        self.filecode = result.get('file_code', result.get('file_code', None))
        self.url = result.get('link', result.get('url', None))

class LongFile:

    def __init__(self, resp):

        self.raw = resp
        self._deserialize(resp)

    def _deserialize(self, resp):
        """Deserializes the json data to python objects.

        Takes a json object as input and maos the keys to the class attributes.
        Parameters:
            -resp : json object
        """
        
        # Fields common to 'List File' and 'List Folder' call response.
        self.filecode = resp.get('file_code', resp.get('filecode', None))
        self.url = resp.get('link', resp.get('url', None))
        self.folder_id = int(resp.get('fld_id')) if resp.get('fld_id', False) else None
        self.title = resp.get('title', None)
        self.canplay = True if int(resp.get('canplay', 0)) else False
        try:
            # Creation date name is Inconsistet in response. 
            self.created = datetime.fromisoformat(
                    resp.get('created', resp.get('uploaded', ''))
                    )
        except ValueError:
            self.created = None

        # Fields only present in List File call Response.
        if resp.get('thumbnail', None):
            self.thumbnail = resp.get('thumbnail', None)
        if resp.get('length', 0):
            self.length = int(resp.get('length',0))
        if resp.get('views', 0):
            self.views = int(resp.get('views', 0))
        if resp.get('public', 0):
            self.public = True if int(resp.get('public', 0)) else False

class FileInfo:

    def __init__(self, resp):
        self.raw = resp
        self._deserialize(self.raw)
    
    def _deserialize(self, resp):
        """Deserializes the json data to python objects.

        Takes a json object as input and maos the keys to the class attributes.
        Parameters:
            -resp : json object
        """

        self.status = resp.get('status', None)
        self.filecode =resp.get('file_code', None)
        self.last_download = resp.get('file_last_download', None)
        self.canplay = True if int(resp.get('canplay', 0)) else False
        self.public = True if int(resp.get('public', 0)) else False
        self.length = int(resp.get('file_length', None))
        self.title = resp.get('file_title', '')
        self.views = int(resp.get('file_views', 0))
        self.name = resp.get('file_name', '')
        #self.created = resp.get('file_created', '')
        try:
            self.created = datetime.fromisoformat(resp.get('file_created', ''))
        except ValueError:
            self.created = None
        self.adult = True if resp.get('file_adult', 0) else False
        
        # These fields are not documented but seen in response.
        self.full_views = int(resp.get('file_views_full',0))
        self.cat_id = int(resp.get('cat_id'))
        self.player_image = resp.get('player_img',None)

class FileList:

    def __init__(self, resp):

        self.raw = resp
        self.results = resp['result'].get('results', 0)
        self.total_results = int(resp['result'].get('results_total', 0)
        self._deserialize_list(resp.get('result',{}))

    def _deserialize_list(self, result):

        self.files = []
        for file in result.get('files', {}):
            self.files.append(LongFile(file))

class Quality:

    url = None
    size = None

    def __init__(self, resp: dict = {}):

        if resp:
            self.raw = resp
            self.url = resp.get('url', None)
            self.size = int(resp.get('size', 0))
