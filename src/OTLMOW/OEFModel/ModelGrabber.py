import json
from pathlib import Path

import requests


class ModelGrabber:
    def __init__(self, requester=requests.Session):
        self.requester = requester

    def grab_models_as_json(self, save_legacy_to: Path = Path('oef.legacy.json'), save_ins_ond_to: Path = Path('oef.ins.ond.json')):
        model = self.requester.get(url='https://services.apps.mow.vlaanderen.be/eminfra/core/api/otl/schema/oef/legacy')
        with open(str(save_legacy_to), 'wb') as f:
            f.write(model.content)

        model = self.requester.get(url='https://services.apps.mow.vlaanderen.be/eminfra/core/api/otl/schema/oef/inspectie-en-onderhoud')
        with open(str(save_ins_ond_to), 'wb') as f:
            f.write(model.content)

    @staticmethod
    def decode_json_and_get_classes(file_path: Path = None):
        f = open(str(file_path))
        dict_obj = json.load(f)
        f.close()
        return dict_obj["classes"]

    @staticmethod
    def decode_json_and_get_attributen(file_path: Path = None):
        f = open(str(file_path))
        dict_obj = json.load(f)
        f.close()
        return dict_obj["attributen"]
