import json

from OTLModel.BaseClasses.OTLAsset import OTLAsset
from OTLModel.Classes.RelatieObject import RelatieObject
from OTLModel.BaseClasses.OTLField import OTLField


class OtlAssetJSONEncoder(json.JSONEncoder):
    def default(self, otlObject):
        if isinstance(otlObject, OTLAsset) or isinstance(otlObject, RelatieObject):
            d = dir(otlObject)
            dictCopy = {}
            for key in d:
                if key[0] == '_' or key == 'attr_info' or key == 'attr_type_info':
                    pass
                else:
                    value = otlObject.__getattribute__(key)
                    if value is None:
                        continue
                    if key == 'deprecated_version':
                        continue
                    if key == 'typeURI':
                        dictCopy['typeURI'] = otlObject.typeURI
                    else:
                        attribute = otlObject.__getattribute__('_' + key)
                        defaultValue = attribute.default()
                        if defaultValue is not None:
                            if isinstance(defaultValue, str):
                                if len(defaultValue) == 0:
                                    continue
                            if isinstance(defaultValue, list):
                                if len(defaultValue) == 0:
                                    continue
                            if isinstance(defaultValue, dict):
                                if self.isEmptyDict(defaultValue):
                                    continue
                            dictCopy[key] = defaultValue
            return dictCopy
        return super().default(otlObject)

    def default2(self, otlObject):
        if isinstance(otlObject, OTLAsset) or isinstance(otlObject, RelatieObject):
            d = dir(otlObject)
            dictCopy = {}
            for key in d:
                if key[0] == '_':
                    pass
                else:
                    value = otlObject.__getattribute__(key)
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
                        dictCopy[key] = valueByDefault
                    else:
                        if value is None:
                            continue
                        dictCopy[key] = value
            return dictCopy
        else:
            return super().default(otlObject)

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

    def write_json_to_file(self, encoded_json, file_path):
        with open(file_path, "w") as file:
            file.write(encoded_json)
