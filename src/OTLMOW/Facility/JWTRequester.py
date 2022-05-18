import datetime
import json
import requests
import string
import jwt  # pip install jwt then Pyjwt

from random import choice
from requests import Response


class JWTRequester(requests.Session):
    def __init__(self, private_key_path='', client_id='', first_part_url=''):
        self.private_key_path = private_key_path
        self.client_id = client_id
        self.first_part_url = first_part_url
        self.oAuth_token = ''
        self.expires = datetime.datetime.now()
        super().__init__()

    def get(self, url='', **kwargs) -> Response:
        kwargs = self.modify_kwargs_for_bearer_token(kwargs)
        return super().get(url=self.first_part_url + url, **kwargs)

    def post(self, url='', **kwargs) -> Response:
        kwargs = self.modify_kwargs_for_bearer_token(kwargs)
        return super().post(url=self.first_part_url + url, **kwargs)

    def put(self, url='', **kwargs) -> Response:
        kwargs = self.modify_kwargs_for_bearer_token(kwargs)
        return super().put(url=self.first_part_url + url, **kwargs)

    def patch(self, url='', **kwargs) -> Response:
        kwargs = self.modify_kwargs_for_bearer_token(kwargs)
        return super().patch(url=self.first_part_url + url, **kwargs)

    def delete(self, url='', **kwargs) -> Response:
        kwargs = self.modify_kwargs_for_bearer_token(kwargs)
        return super().delete(url=self.first_part_url + url, **kwargs)

    def get_oAuth_token(self) -> str:
        if self.is_token_valid():
            return self.oAuth_token

        authentification_token = self.generate_authentification_token()
        self.oAuth_token = self.get_access_token(authentification_token)
        self.expires = datetime.datetime.now() + datetime.timedelta(minutes=59)

        return self.oAuth_token

    def is_token_valid(self) -> bool:
        if self.expires > datetime.datetime.now():
            return True
        return False

    def modify_kwargs_for_bearer_token(self, kwargs: dict) -> dict:
        bearer_token = self.get_oAuth_token()
        if 'headers' not in kwargs:
            kwargs['headers'] = {}

        for arg in kwargs:
            if arg == 'headers':
                headers = kwargs[arg]
                if 'accept' not in headers:
                    headers['accept'] = ''
                if headers["accept"] is not None:
                    if headers["accept"] != '':
                        headers["accept"] = headers["accept"] + ", application/json"
                    else:
                        headers["accept"] = "application/json"
                headers["authorization"] = f"Bearer {bearer_token}"
                kwargs['headers'] = headers


        return kwargs

    def generate_authentification_token(self) -> str:
        # Authentification token generation
        payload = {"iss": f"{self.client_id}",
                   "sub": f"{self.client_id}",
                   "aud": "https://authenticatie.vlaanderen.be/op",
                   "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
                   "jti": ''.join(choice(string.ascii_lowercase) for _ in range(20))
                   }

        with open(self.private_key_path) as private_key:
            private_key_json = json.load(private_key)
            key = jwt.algorithms.RSAAlgorithm.from_jwk(private_key_json)
            token = jwt.encode(payload=payload, key=key, algorithm="RS256")

        return token

    def get_access_token(self, token: str) -> str:
        # Authorization access token generation
        url = "https://authenticatie.vlaanderen.be/op/v1/token"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        request_body = {
            "grant_type": "client_credentials",
            "scope": "awv_toep_services",
            "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
            "client_id": f"{self.client_id}",
            "client_assertion": f"{token}"
        }

        response = requests.post(url, data=request_body, headers=headers)

        # Check for HTTP codes other than 200
        if response.status_code != 200:
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.content)
            raise RuntimeError("Could not get the acces token")

        return response.json()["access_token"]