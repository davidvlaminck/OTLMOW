import unittest

from OTLMOW.Facility.Exceptions.CouldNotCreateRelationError import CouldNotCreateRelationError
from OTLMOW.Facility.RelationCreator import RelationCreator
from OTLMOW.OTLModel.Classes.Onderdeel.Aftakking import Aftakking
from OTLMOW.OTLModel.Classes.Onderdeel.EnergiemeterAWV import EnergiemeterAWV
from OTLMOW.OTLModel.Classes.Onderdeel.Voedt import Voedt


class RelationCreatorTests(unittest.TestCase):
    def test_create_valid_relation(self):
        creator = RelationCreator()
        e = EnergiemeterAWV()
        e.assetId.identificator = 'e'
        a = Aftakking()
        a.assetId.identificator = 'a'
        v = Voedt
        relatie = creator.create_relation(bron=e, doel=a, relatie=v)
        self.assertIsNotNone(relatie)
        self.assertEqual(relatie.typeURI, v.typeURI)
        self.assertEqual(relatie.bronAssetId.identificator, e.assetId.identificator)
        self.assertEqual(relatie.doelAssetId.identificator, a.assetId.identificator)

    def test_create_invalid_relation(self):
        creator = RelationCreator()
        e = EnergiemeterAWV()
        e.assetId.identificator = 'e'
        a = Aftakking()
        a.assetId.identificator = 'a'
        v = Voedt
        with self.assertRaises(CouldNotCreateRelationError):
            relatie = creator.create_relation(bron=a, doel=e, relatie=v)

    #TODO add test for deprecation warning

