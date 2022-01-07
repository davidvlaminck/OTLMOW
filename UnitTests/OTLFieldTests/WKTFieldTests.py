import unittest

from OTLModel.BaseClasses.WKTField import WKTField
from OTLModel.Datatypes.DtcRechtspersoon import DtcRechtspersoon
from OTLModel.Datatypes.DtcIdentificator import DtcIdentificator


class WktTestClass:
    def __init__(self):
        self.wkt = WKTField('','','','','','','')


class ComplexDataTypeFieldTests(unittest.TestCase):
    def test_WKTNone(self):
        instance = WktTestClass()
        instance.wkt.waarde = None

        self.assertIsNone(instance.wkt.waarde)

    def test_WKTInvalid(self):
        instance = WktTestClass()

        with self.assertRaises(ValueError) as e:
            instance.wkt.waarde = '1'

        with self.assertRaises(ValueError) as e:
            instance.wkt.waarde = 1

    def test_WKTValid(self):
        instance = WktTestClass()
        instance.wkt.waarde = 'POINT(1 2)'

        self.assertIsNotNone(instance.wkt.waarde)



