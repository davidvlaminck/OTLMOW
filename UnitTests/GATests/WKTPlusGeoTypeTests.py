import unittest

from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.OTLModel.BaseClasses.OTLAsset import OTLAsset


class PointTestClass(PuntGeometrie, OTLAsset):
    def __init__(self):
        super().__init__()


class WKTPlusGeoTypeTests(unittest.TestCase):
    def test_Point(self):
        puntclass = PointTestClass()

        with self.subTest('valid point'):
            puntclass.geometry = 'POINT Z(1 2 3)'
            self.assertIsNotNone(puntclass.geometry)

        with self.subTest('invalid points'):
            with self.assertRaises(TypeError):
                puntclass.geometry = 'POINT(1 2)'
            with self.assertRaises(ValueError):
                puntclass.geometry = 'POINT Z(1 2,0 3)'

# TODO add more test for other types
