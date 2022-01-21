import json
from collections import OrderedDict

from OTLModel.BaseClasses.OTLAsset import OTLAsset
from OTLModel.BaseClasses.OTLObject import OTLObject
from OTLModel.Classes.RelatieObject import RelatieObject
from OTLModel.BaseClasses.OTLField import OTLField


class OtlAssetJSONEncoder(json.JSONEncoder):
    def default(self, otlObject):
        if isinstance(otlObject, OTLObject):
            d = otlObject.create_dict_from_asset()
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
