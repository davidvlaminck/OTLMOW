import json

import requests


class ModelGrabber:
    def __init__(self):
        self.cert_path = 'C:\\resources\\datamanager_eminfra_prd.awv.vlaanderen.be.crt'
        self.key_path = 'C:\\resources\\datamanager_eminfra_prd.awv.vlaanderen.be.key'

    def grab_model(self, save_to: str = 'oef.legacy.json'):
        model = requests.get('https://services.apps.mow.vlaanderen.be/eminfra/core/api/otl/schema/oef/legacy',  cert=(self.cert_path, self.key_path))
        with open(save_to, 'wb') as f:
            f.write(model.content)

    def decode_json_and_get_classes(self, file_path: str = ''):
        f = open(file_path)
        dict_obj = json.load(f)
        f.close()
        return dict_obj["classes"]

    def decode_json_and_get_attributen(self, file_path: str = ''):
        f = open(file_path)
        dict_obj = json.load(f)
        f.close()
        return dict_obj["attributen"]