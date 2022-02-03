import unittest

from OTLMOW.OTLModel.BaseClasses.OTLAsset import OTLAsset
from OTLMOW.OTLModel.BaseClasses.WKTValidator import WKTValidator


class ComplexDataTypeFieldTests(unittest.TestCase):
    def test_WKT_valid(self):
        with self.subTest('testen POINT'):
            self.assertTrue(WKTValidator.validate_wkt("POINT (1.0 2.0)"))
            self.assertTrue(WKTValidator.validate_wkt("POINT (1 2)"))
            self.assertTrue(WKTValidator.validate_wkt("POINT (12345.678901 12345.678902)"))
            self.assertTrue(WKTValidator.validate_wkt("POINT Z (1.0 2.0 3.0)"))
            self.assertTrue(WKTValidator.validate_wkt("POINT Z (1 2 3)"))
            self.assertFalse(WKTValidator.validate_wkt("POINT Z (1,0 2,0 3,0)"))
            self.assertFalse(WKTValidator.validate_wkt("POINT Z (1 2)"))
            self.assertFalse(WKTValidator.validate_wkt("POINT (1 2 3)"))
            self.assertFalse(WKTValidator.validate_wkt("POINT(1 2)"))
            self.assertFalse(WKTValidator.validate_wkt("POINT (-1 -2)"))
            self.assertFalse(WKTValidator.validate_wkt("punt Z (1 2)"))

        with self.subTest('testen LINESTRING'):
            self.assertTrue(WKTValidator.validate_wkt("LINESTRING (1.0 2.0, 3.0 4.0)"))
            self.assertTrue(WKTValidator.validate_wkt("LINESTRING (1 2, 3 4)"))
            self.assertTrue(WKTValidator.validate_wkt("LINESTRING Z (1.0 2.0 3.0, 4.0 5.0 6.0)"))
            self.assertTrue(WKTValidator.validate_wkt("LINESTRING Z (1.0 2.0 3.0, 4.0 5.0 6.0, 7.0 8.0 9.0)"))
            self.assertTrue(WKTValidator.validate_wkt("LINESTRING Z (1 2 3, 4 5 6, 7 8 9)"))
            self.assertFalse(WKTValidator.validate_wkt("LINESTRING (1,0 2,0, 3,0 4,0)"))
            self.assertFalse(WKTValidator.validate_wkt("LINESTRING Z (1.0 2.0, 4.0 5.0)"))
            self.assertFalse(WKTValidator.validate_wkt("LINESTRING (1 2 5, 3 4 6)"))

        with self.subTest('testen POLYGON'):
            self.assertTrue(WKTValidator.validate_wkt("POLYGON ((10 20, 30 40, 50 60))"))
            self.assertFalse(WKTValidator.validate_wkt("POLYGON ((10 20, 30 40))"))
            self.assertTrue(WKTValidator.validate_wkt("POLYGON ((10.0 20.0, 30.0 40.0, 50.0 60.0))"))
            self.assertTrue(WKTValidator.validate_wkt("POLYGON ((10.0 20.0, 30.0 40.0, 50.0 60.0, 70.0 80.0))"))
            self.assertTrue(WKTValidator.validate_wkt("POLYGON Z ((10.0 20.0 1, 30.0 40.0 2, 50.0 60.0 3))"))
            self.assertFalse(WKTValidator.validate_wkt("POLYGON Z ((10.0 20.0, 30.0 40.0 2, 50.0 60.0))"))
            self.assertFalse(WKTValidator.validate_wkt("POLYGON ((10.0 20.0 1, 30.0 40.0 2, 50.0 60.0 3))"))
            self.assertTrue(
                WKTValidator.validate_wkt("POLYGON ((10.0 20.0, 30.0 40.0, 50.0 60.0), (110.0 120.0, 130.0 140.0, 150.0 160.0))"))
