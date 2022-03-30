import os
import requests
from requests import Response


class CertRequester(requests.Session):
    def __init__(self, cert_path='', key_path='', first_part_url=''):
        super().__init__()
        self.cert_path = cert_path
        self.key_path = key_path
        self.first_part_url = first_part_url

        if not os.path.isfile(cert_path):
            raise FileNotFoundError(cert_path + " is not a valid path. Cert file does not exist.")
        if not os.path.isfile(key_path):
            raise FileNotFoundError(key_path + " is not a valid path. Key file does not exist.")

    def get(self, url='', **kwargs) -> Response:
        return super().get(url=self.first_part_url + url, cert=(self.cert_path, self.key_path), **kwargs)

    def post(self, url='', **kwargs) -> Response:
        return super().post(url=self.first_part_url + url, cert=(self.cert_path, self.key_path), **kwargs)

    def put(self, url='', **kwargs) -> Response:
        return super().put(url=self.first_part_url + url, cert=(self.cert_path, self.key_path), **kwargs)

    def patch(self, url='', **kwargs) -> Response:
        return super().patch(url=self.first_part_url + url, cert=(self.cert_path, self.key_path), **kwargs)

    def delete(self, url='', **kwargs) -> Response:
        return super().delete(url=self.first_part_url + url, cert=(self.cert_path, self.key_path), **kwargs)
