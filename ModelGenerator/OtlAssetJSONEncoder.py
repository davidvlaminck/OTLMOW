import json

from ModelGenerator.BaseClasses.ComplexField import ComplexField
from ModelGenerator.BaseClasses.KeuzelijstField import KeuzelijstField
from ModelGenerator.BaseClasses.OTLAsset import OTLAsset
from ModelGenerator.BaseClasses.OTLField import OTLField
from OTLClasses.Verification.DtcIdentificator import ComplexAttributen


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
                        dictCopy[key] = value.default()
                    else:
                        dictCopy[key] = value
            return dictCopy
        else:
            return super().default(otlAsset)
    # https://realpython.com/python-json/?fbclid=IwAR2gXW0-lF6Koyd6YxpSUBJH-mEj1lS1lEPUavPfrYbzfbzWnkLcRN_RAG8