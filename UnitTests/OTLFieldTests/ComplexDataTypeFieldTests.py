import unittest

from OTLModel.Datatypes.DtcRechtspersoon import DtcRechtspersoon
from OTLModel.Datatypes.DtcIdentificator import DtcIdentificator


class DtcTestClass:
    def __init__(self):
        self.dtcTestType = DtcIdentificator()
        self.dtcPersoon = DtcRechtspersoon()


class ComplexDataTypeFieldTests(unittest.TestCase):
    def test_DtcIdentificator(self):
        instance = DtcTestClass()
        instance.dtcTestType.identificator.waarde = "abc"
        instance.dtcTestType.toegekendDoor.waarde = "def"
        self.assertEqual("abc", instance.dtcTestType.identificator.waarde)
        self.assertEqual("def", instance.dtcTestType.toegekendDoor.waarde)

    def test_dtcPersoon(self):
        instance = DtcTestClass()
        instance.dtcPersoon.afdeling.waarde = "afdeling"
        self.assertEqual("afdeling", instance.dtcPersoon.afdeling.waarde)
        self.assertEqual("afdeling", instance.dtcPersoon.waarde.afdeling.waarde)

        instance.dtcPersoon.adres.straatnaam.waarde = "straat"
        self.assertEqual("straat", instance.dtcPersoon.adres.straatnaam.waarde)
        self.assertEqual("straat", instance.dtcPersoon.waarde.adres.waarde.straatnaam.waarde)


