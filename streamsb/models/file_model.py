from datetime import datetime

class File:

    def __init__(self, resp):

        self.raw = resp
        result = res.get('result', {})
        # API is inconsistent with file code 
        # Noticed variations = ['file_code', 'filecode']
        self.filecode = result.get('file_code', result.get('file_code', None))
        self.url = result.get('link', result.get('url', None))

class LongFile(File):

    def __init__(self, resp):

        super().__init(resp)
        self._deserialize(resp)

    def _deserialize(self, resp):
        """Deserializes the json data to python objects.

        Takes a json object as input and maos the keys to the class attributes.
        Parameters:
            -resp : json object
        """



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
        self.canplay = True if resp.get('canplay', 0) else False
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
