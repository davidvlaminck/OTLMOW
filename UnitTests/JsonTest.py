import json
import unittest

from ModelGenerator.BaseClasses.KeuzelijstField import KeuzelijstField
from ModelGenerator.BaseClasses.OTLAsset import OTLAsset
from ModelGenerator.BaseClasses.OTLField import OTLField
from ModelGenerator.BaseClasses.RelatieValidator import RelatieValidator
from OTLClasses.Verification.Aftakking import Aftakking
from UnitTests.RelatieValidatorTests import GeldigeRelatieLijstTestInstance


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
                    if isinstance(value, KeuzelijstField):
                        dictCopy[key] = value.waarde.invulwaarde
                    elif isinstance(value, OTLField):
                        dictCopy[key] = value.waarde
                    else:
                        dictCopy[key] = value
            return dictCopy
        else:
            return super().default(otlAsset)
    # https://realpython.com/python-json/?fbclid=IwAR2gXW0-lF6Koyd6YxpSUBJH-mEj1lS1lEPUavPfrYbzfbzWnkLcRN_RAG8


class JsonTests(unittest.TestCase):
    def test_JsonEncode(self):
        # add _geldige_relaties on Aftakking type
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)

        # create testable OTLAsset
        a = Aftakking()
        a.naam.waarde = "aftakking"
        a.notitie.waarde = "notitie aftakking"
        a.isActief.waarde = True
        a.toestand.set_value_by_label("in ontwerp")

        encoder = OtlAssetJSONEncoder()
        js = encoder.encode(a)

        self.assertEqual('{"isActief": true, "naam": "aftakking", "notitie": "notitie aftakking", "toestand": "in-ontwerp", "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking"}', js)
