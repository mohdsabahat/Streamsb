import requests

class APISession(requests.Session):

    def __init__(self, *args, **kwargs):
        super(APISession, self).__init__(*args, **kwargs)
        """
        self.headers.update({
            'Accept-Charset': 'utf-8',
            'Content-Type': 'text/plain',
            'User-Agent': 'factom-api/{}'.format(VERSION)
        })
        """
