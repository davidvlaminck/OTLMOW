import unittest

from OTLModel.Verification.DtcIdentificator import DtcIdentificator


class DtcTestClass:
    def __init__(self):
        self.dtcTestType = DtcIdentificator()


class ComplexDataTypeFieldTests(unittest.TestCase):
    def test_InitField(self):
        instance = DtcTestClass()
        instance.dtcTestType.identificator = "abc"
        instance.dtcTestType.toegekendDoor = "def"
        self.assertEqual("abc", instance.dtcTestType.identificator)
        self.assertEqual("def", instance.dtcTestType.toegekendDoor)
