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
                        if value.default() is None:
                            continue
                        dictCopy[key] = value.default()
                    else:
                        if value is None:
                            continue
                        dictCopy[key] = value
            return dictCopy
        else:
            return super().default(otlAsset)
    # https://realpython.com/python-json/?fbclid=IwAR2gXW0-lF6Koyd6YxpSUBJH-mEj1lS1lEPUavPfrYbzfbzWnkLcRN_RAG8