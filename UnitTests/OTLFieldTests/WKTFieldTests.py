﻿import unittest

from OTLModel.BaseClasses.OTLAsset import OTLAsset
from OTLModel.BaseClasses.WKTField import WKTField
from OTLModel.Datatypes.DtcRechtspersoon import DtcRechtspersoon
from OTLModel.Datatypes.DtcIdentificator import DtcIdentificator


class WktTestClass(OTLAsset):
    def __init__(self):
        super().__init__()


class ComplexDataTypeFieldTests(unittest.TestCase):
    def test_WKTNone(self):
        instance = WktTestClass()
        instance.geometry = None

        self.assertIsNone(instance.geometry)

    def test_WKTInvalid(self):
        instance = WktTestClass()

        with self.assertRaises(ValueError) as e:
            instance.geometry = '1'

        with self.assertRaises(TypeError) as e:
            instance.geometry = 1

    def test_WKTValid(self):
        instance = WktTestClass()
        instance.geometry = 'POINT(1 2)'

        self.assertIsNotNone(instance.geometry)



