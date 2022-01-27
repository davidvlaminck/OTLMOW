import unittest
from unittest import TestCase

from OTLMOW.OTLModel.Classes.Wegkantkast import Wegkantkast


class WrongGeometryError(Exception):
    pass


@unittest.skip("feature request")
class GeometryArtefactIntegration(TestCase):
    def test_invalid_geometry_based_on_geometry_artefact(self):
        w = Wegkantkast()
        with self.assertRaises(WrongGeometryError) as wrong_geometry_exception:
            w.geometry = 'LINESTRING Z (100000 200000 10, 300000 400000 20)'
        error_msg = "Asset type Wegkantkast can't be assigned a line as geometry, valid types are point and polygon"
        self.assertEqual(error_msg, str(wrong_geometry_exception.exception))
