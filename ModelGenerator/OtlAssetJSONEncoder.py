import json

from OTLModel.BaseClasses.OTLAsset import OTLAsset
from OTLModel.Datatypes.OTLField import OTLField


class OtlAssetJSONEncoder(json.JSONEncoder):
    def default(self, otlAsset):
        if isinstance(otlAsset, OTLAsset):
            d = dir(otlAsset)
            dictCopy = {}
            for key in d:
                if key[0] == '_':
                    pass
                else:
                    value = otlAsset.__getattribute__(key)
                    if isinstance(value, OTLField):
                        valueByDefault = value.default()
                        if valueByDefault is None:
                            continue
                        if isinstance(valueByDefault, str):
                            if len(valueByDefault) == 0:
                                continue
                        if isinstance(valueByDefault, list):
                            if len(valueByDefault) == 0:
                                continue
                        if isinstance(valueByDefault, dict):
                            if self.isEmptyDict(valueByDefault):
                                continue
                        dictCopy[key] =valueByDefault
                    else:
                        if value is None:
                            continue
                        dictCopy[key] = value
            return dictCopy
        else:
            return super().default(otlAsset)

    # https://realpython.com/python-json/?fbclid=IwAR2gXW0-lF6Koyd6YxpSUBJH-mEj1lS1lEPUavPfrYbzfbzWnkLcRN_RAG8

    def isEmptyDict(self, value: dict):
        b = True
        for v in value.values():
            if isinstance(v, dict):
                if self.isEmptyDict(v):
                    continue
            if v is not None:
                return False
        return b
