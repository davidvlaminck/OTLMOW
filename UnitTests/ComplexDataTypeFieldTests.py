import unittest

from OTLClasses.Verification.DtcIdentificator import DtcIdentificator


class DtcTestClass:
    dtcTestType: DtcIdentificator

    def __init__(self):
        self.dtcTestType = DtcIdentificator(naam="DtcIdentificator", label="DtcIdentificator",
                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DtcIdentificator",
                            definition="DtcIdentificator definitie"
                            , constraints="", usagenote="", deprecated_version="")


class ComplexDataTypeFieldTests(unittest.TestCase):
    def test_InitField(self):
        instance = DtcTestClass()
        instance.dtcTestType.identificator = "abc"
        instance.dtcTestType.toegekendDoor = "def"

