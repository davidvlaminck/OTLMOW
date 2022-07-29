import json

import requests


class ModelGrabber:
    def __init__(self, requester=requests.Session):
        self.requester = requester

    def grab_models_as_json(self, save_legacy_to: str = 'oef.legacy.json', save_ins_ond_to: str = 'oef.ins.ond.json'):
        model = self.requester.get('https://services.apps.mow.vlaanderen.be/eminfra/core/api/otl/schema/oef/legacy')
        with open(save_legacy_to, 'wb') as f:
            f.write(model.content)

        model = self.requester.get('https://services.apps.mow.vlaanderen.be/eminfra/core/api/otl/schema/oef/inspectie-en-onderhoud')
        with open(save_ins_ond_to, 'wb') as f:
            f.write(model.content)

    @staticmethod
    def decode_json_and_get_classes(file_path: str = ''):
        f = open(file_path)
        dict_obj = json.load(f)
        f.close()
        return dict_obj["classes"]

    @staticmethod
    def decode_json_and_get_attributen(file_path: str = ''):
        f = open(file_path)
        dict_obj = json.load(f)
        f.close()
        return dict_obj["attributen"]
