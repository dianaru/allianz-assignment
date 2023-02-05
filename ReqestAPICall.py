import requests


class ReqestAPICall(object):
    def __init__(self, base_url) -> None:
        self._base_url = base_url
        self.session = requests.Session()
        
    #region Properties
    @property
    def base_url(self):
        return self._base_url
    @base_url.setter
    def base_url(self, value):
        self._base_url = value
    #endregion

    def get(self, url, **kwargs):
        try:
            return self.session.get(self.base_url+url, **kwargs)
        except requests.exceptions.RequestException as e:
            print(e.response.text)
    def post(self, url, **kwargs):
        try:
            return self.session.post(self.base_url+url, **kwargs)
        except requests.exceptions.RequestException as e:
            print(e.response.text)

    def put(self, url, **kwargs):
        try:
            return self.session.put(self.base_url+url, **kwargs)
        except requests.exceptions.RequestException as e:
            print(e.response.text)
    def delete(self, url, **kwargs):
        try:
            return self.session.delete(self.base_url+url, **kwargs)
        except requests.exceptions.RequestException as e:
            print(e.response.text)
    