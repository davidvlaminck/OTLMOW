import unittest
from abc import ABC, abstractmethod

from OTLClasses.Verification.AIMObject import AIMObject
from OTLClasses.Verification.DtcAdres import DtcAdres


class testClass(AIMObject):
    def __init__(self):
        AIMObject.__init__(self)
        self.testAdres = DtcAdres(naam="testAdres", label="atestAdres",
                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#testAdres",
                            definition="testAdres definitie"
                            , constraints="", usagenote="", deprecated_version="")

class DtcAdresTests(unittest.TestCase):
    def test_UseInClass(self):
        instance = testClass()
        instance.testAdres.bus.waarde = "A"
        self.assertTrue(instance.testAdres.bus.waarde == "A")
        instance.testAdres.waarde = "adres"
        self.assertTrue(instance.testAdres.waarde == "adres")
        self.assertTrue(instance.testAdres.bus.waarde == "A")
        instance.testAdres.bus.waarde = "B"
        self.assertTrue(instance.testAdres.bus.waarde == "B")

    def test_DtcAdresInit(self):
        adres = DtcAdres()

        adres.bus.waarde = "A"
        self.assertTrue(adres.bus.waarde == "A")

        adres.gemeente.set_value_by_label("de Haan")
        self.assertTrue(adres.gemeente.value.waarde == "de-Haan")

        adres.huisnummer.waarde = "1"
        self.assertTrue(adres.huisnummer.waarde == "1")
        with self.assertRaises(ValueError):
            adres.huisnummer.waarde = 1

        adres.postcode.waarde = "2880"
        self.assertTrue(adres.postcode.waarde == "2880")
        with self.assertRaises(ValueError):
            adres.postcode.waarde = 2880
