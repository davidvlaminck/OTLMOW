import json
from collections import OrderedDict

from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObject


class OtlAssetJSONEncoder(json.JSONEncoder):
    def __init__(self, indent=None, settings=None):
        super().__init__(indent=indent)
        if settings is None:
            settings = {}
        self.settings = settings

        if 'file_formats' not in self.settings:
            raise ValueError("The settings are not loaded or don't contain settings for file formats")
        json_settings = next((s for s in settings['file_formats'] if 'name' in s and s['name'] == 'json'), None)
        if json_settings is None:
            raise ValueError("Unable to find json in file formats settings")

        self.settings = json_settings

    def default(self, otlObject):
        if isinstance(otlObject, OTLObject):
            d = otlObject.create_dict_from_asset(waarde_shortcut=self.settings['dotnotatie']['waarde_shortcut_applicable'])
            if hasattr(otlObject, 'typeURI'):
                d['typeURI'] = otlObject.typeURI
            od = OrderedDict(sorted(d.items()))
            return od
        return super().default(otlObject)

    # no usage?
    def isEmptyDict(self, value: dict):
        b = True
        for v in value.values():
            if isinstance(v, dict):
                if self.isEmptyDict(v):
                    continue
            if v is not None:
                return False
        return b

    def write_json_to_file(self, encoded_json, file_path):
        with open(file_path, "w") as file:
            file.write(encoded_json)
