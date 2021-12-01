import unittest

from OTLClasses.Verification.DtcIdentificator import DtcIdentificator


class DtcTestClass:
    dtcTestType: DtcIdentificator

    def __init__(self):
        self.dtcTestType = DtcIdentificator()


class ComplexDataTypeFieldTests(unittest.TestCase):
    def test_InitField(self):
        instance = DtcTestClass()
        instance.dtcTestType.identificator = "abc"
        instance.dtcTestType.toegekendDoor = "def"

