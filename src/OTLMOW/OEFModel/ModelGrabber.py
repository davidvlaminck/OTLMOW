import json

import requests


class ModelGrabber:
    def __init__(self):
        self.cert_path = 'C:\\resources\\datamanager_eminfra_prd.awv.vlaanderen.be.crt'
        self.key_path = 'C:\\resources\\datamanager_eminfra_prd.awv.vlaanderen.be.key'

    def grab_models_as_json(self, save_legacy_to: str = 'oef.legacy.json', save_ins_ond_to: str = 'oef.ins.ond.json'):
        model = requests.get('https://services.apps.mow.vlaanderen.be/eminfra/core/api/otl/schema/oef/legacy',
                             cert=(self.cert_path, self.key_path))
        with open(save_legacy_to, 'wb') as f:
            f.write(model.content)

        model = requests.get('https://services.apps.mow.vlaanderen.be/eminfra/core/api/otl/schema/oef/inspectie-en-onderhoud',
                             cert=(self.cert_path, self.key_path))
        with open(save_ins_ond_to, 'wb') as f:
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
