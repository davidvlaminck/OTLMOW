import unittest

from OTLMOW.Facility.Exceptions.WrongGeometryError import WrongGeometryError
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie
from OTLMOW.OTLModel.BaseClasses.OTLAsset import OTLAsset


class PointTestClass(PuntGeometrie, OTLAsset):
    typeURI = '#PointTestClass'
    def __init__(self):
        PuntGeometrie.__init__(self)
        OTLAsset.__init__(self)


class PointPolygonTestClass(PuntGeometrie, VlakGeometrie, OTLAsset):
    typeURI = '#PointPolygonTestClass'
    def __init__(self):
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)
        OTLAsset.__init__(self)


class WKTPlusGeoTypeTests(unittest.TestCase):
    def test_point(self):
        puntclass = PointTestClass()

        with self.subTest('valid point'):
            puntclass.geometry = 'POINT Z (1 2 3)'
            self.assertIsNotNone(puntclass.geometry)

        with self.subTest('invalid points'):
            with self.assertRaises(WrongGeometryError):
                puntclass.geometry = 'POINT (1 2)'
            with self.assertRaises(ValueError):
                puntclass.geometry = 'POINT Z (1 2,0 3)'

    def test_point_polygon(self):
        puntvlakclass = PointPolygonTestClass()

        with self.subTest('valid point'):
            puntvlakclass.geometry = 'POINT Z (1 2 3)'
            self.assertIsNotNone(puntvlakclass.geometry)

        with self.subTest('valid polygon'):
            puntvlakclass.geometry = 'POLYGON Z ((10.0 20.0 1, 30.0 40.0 2, 50.0 60.0 3))'
            self.assertIsNotNone(puntvlakclass.geometry)

        with self.subTest('invalid points'):
            with self.assertRaises(WrongGeometryError):
                puntvlakclass.geometry = 'POINT (1 2)'
            with self.assertRaises(ValueError):
                puntvlakclass.geometry = 'POINT Z (1 2,0 3)'

        with self.subTest('invalid polygons'):
            with self.assertRaises(WrongGeometryError):
                puntvlakclass.geometry = 'POLYGON ((10 20, 30 40, 50 60))'
            with self.assertRaises(ValueError):
                puntvlakclass.geometry = 'POLYGON Z ((10.0 20.0, 30.0 40.0 2, 50.0 60.0))'
