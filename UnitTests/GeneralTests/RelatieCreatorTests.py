import unittest

from OTLMOW.Facility.AssetFactory import AssetFactory
from OTLMOW.Facility.Exceptions.CouldNotCreateRelation import CouldNotCreateRelation
from OTLMOW.Facility.RelatieCreator import RelatieCreator
from OTLMOW.ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie
from OTLMOW.ModelGenerator.BaseClasses.RelatieValidator import RelatieValidator
from OTLMOW.OTLModel.BaseClasses.RelatieInteractor import RelatieInteractor
from OTLMOW.OTLModel.Classes.Onderdeel.Aftakking import Aftakking
from OTLMOW.OTLModel.Classes.Onderdeel.EnergiemeterAWV import EnergiemeterAWV
from OTLMOW.OTLModel.Classes.ImplementatieElement.RelatieObject import RelatieObject
from OTLMOW.OTLModel.Classes.Onderdeel.Voedt import Voedt


class GeldigeRelatieLijst:
    def __init__(self):
        self.lijst = []


class UriToClassNameLijst:
    def __init__(self):
        self.dict = {
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterAWV': 'EnergiemeterAWV',
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking': 'Aftakking',
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt': 'Voedt',
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring': 'Stroomkring',
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoofdschakelaar': 'Hoofdschakelaar',
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor': 'Contactor'
        }


class GeldigeRelatie2:
    def __init__(self, bron: str, doel: str, relatie: str):
        classLoader = AssetFactory()

        bronClassName = UriToClassNameLijst().dict[bron]
        bronInstance = classLoader.dynamic_create_instance_from_ns_and_name(bronClassName)
        if not (isinstance(bronInstance, RelatieInteractor)):
            raise TypeError("parameter bron is geen AbstractRelatieInteractor")

        doelClassName = UriToClassNameLijst().dict[doel]
        doelInstance = classLoader.dynamic_create_instance_from_ns_and_name(doelClassName)
        if not (isinstance(doelInstance, RelatieInteractor)):
            raise TypeError("parameter doel is geen AbstractRelatieInteractor")

        relatieClassName = UriToClassNameLijst().dict[relatie]
        relatieInstance = classLoader.dynamic_create_instance_from_ns_and_name(relatieClassName)
        if not (isinstance(relatieInstance, RelatieObject)):
            raise TypeError("parameter relatie is geen RelatieObject")

        self.relatie = relatie
        self.doel = doel
        self.bron = bron


class GeldigeRelatieLijstTestInstance(GeldigeRelatieLijst):
    def __init__(self):
        GeldigeRelatieLijst.__init__(self)
        self.lijst = [
            GeldigeRelatie('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterAWV',
                           'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking',
                           'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt',
                           ''),
            GeldigeRelatie('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring',
                           'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking',
                           'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt',
                           ''),
            GeldigeRelatie('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking',
                           'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoofdschakelaar',
                           'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt',
                           ''),
            GeldigeRelatie('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring',
                           'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor',
                           'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt',
                           ''),
            GeldigeRelatie('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking',
                           'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoofdschakelaar',
                           'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging',
                           'deprecated')
        ]


class RelatieValidatorTests(unittest.TestCase):
    def test_create_instance(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance().lijst
        validator = RelatieValidator(geldigeRelatieLijst)
        creator = RelatieCreator(validator)
        self.assertIsNotNone(creator)

    def test_create_valid_relation(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance().lijst
        validator = RelatieValidator(geldigeRelatieLijst)
        creator = RelatieCreator(validator)
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
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance().lijst
        validator = RelatieValidator(geldigeRelatieLijst)
        creator = RelatieCreator(validator)
        e = EnergiemeterAWV()
        e.assetId.identificator = 'e'
        a = Aftakking()
        a.assetId.identificator = 'a'
        v = Voedt
        with self.assertRaises(CouldNotCreateRelation):
            relatie = creator.create_relation(bron=a, doel=e, relatie=v)

