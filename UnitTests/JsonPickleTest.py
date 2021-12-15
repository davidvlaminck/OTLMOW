import unittest

import jsonpickle

from OTLModel.Verification.Aftakking import Aftakking


class JsonPickleTests(unittest.TestCase):
    def test_JsonEncode(self):
        a = Aftakking()
        a.naam = "aftakking"
        a.notitie = "notitie aftakking"
        a.typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking"
        a.toestand.set_value_by_label("in ontwerp")
        a.isActief = True

        js = jsonpickle.encode(a);
        print(js)

    def test_JsonDecodePickledString(self):
        result = jsonpickle.decode('{"py/object": "OTLModel.Verification.Aftakking.Aftakking", "isActief": true, "toestand": {"py/object": "OTLModel.Verification.KlAIMToestand.KlAIMToestand", "py/state": "in-ontwerp"}, "notitie": "notitie aftakking", "naam": "aftakking", "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking"}')
        print(result)

    def test_JsonDecodeNoPyObjects(self):
        noPyObjects = '{ "isActief": true, "toestand": null, "notitie": "notitie aftakking", "naam": "aftakking", "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking" }'
        result2 = jsonpickle.decode(noPyObjects)
        print(result2)

    def test_JsonDecodeNoPyObjectToestand(self):
        noPyObjects = '{"py/object": "OTLModel.Verification.Aftakking.Aftakking", "isActief": true, "toestand": null, "notitie": "notitie aftakking", "naam": "aftakking", "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking"}'
        result2 = jsonpickle.decode(noPyObjects)
        print(result2)
        self.assertEqual(result2.isActief, True)
        self.assertEqual(result2.notitie, "notitie aftakking")
        self.assertEqual(result2.typeURI, "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking")
        self.assertEqual(result2.toestand, None)

        noPyObjects = '{"py/object": "OTLModel.Verification.Aftakking.Aftakking", "isActief": true, "toestand": "in-ontwerp", "notitie": "notitie aftakking", "naam": "aftakking", "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking"}'
        result2 = jsonpickle.decode(noPyObjects)
        self.assertEqual(result2.toestand, "in-ontwerp")