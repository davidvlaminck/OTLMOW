import os
import unittest

from OTLMOW.Facility.AssetFactory import AssetFactory
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie
from OTLMOW.ModelGenerator.BaseClasses.RelatieRichting import RelatieRichting
from OTLMOW.ModelGenerator.BaseClasses.RelatieValidator import RelatieValidator
from OTLMOW.OTLModel.BaseClasses.RelatieInteractor import RelatieInteractor
from OTLMOW.OTLModel.Classes.Onderdeel.Aftakking import Aftakking
from OTLMOW.OTLModel.Classes.Onderdeel.Bevestiging import Bevestiging
from OTLMOW.OTLModel.Classes.Onderdeel.Contactor import Contactor
from OTLMOW.OTLModel.Classes.Onderdeel.EnergiemeterAWV import EnergiemeterAWV
from OTLMOW.OTLModel.Classes.Onderdeel.Hoofdschakelaar import Hoofdschakelaar
from OTLMOW.OTLModel.Classes.ImplementatieElement.RelatieObject import RelatieObject
from OTLMOW.OTLModel.Classes.Onderdeel.Stroomkring import Stroomkring
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
    @unittest.skip("only passes when run in a vacuum")
    def test_beforeInitValidateRelatieOnObject(self):
        e = EnergiemeterAWV()
        a = Aftakking()
        v = Voedt
        with self.assertRaises(NotImplementedError):
            self.assertTrue(a._validateRelatiePossible(e, v, RelatieRichting.DOEL_BRON))

    def test_GeldigeRelatieAttrOk(self):
        instance = GeldigeRelatieLijstTestInstance().lijst[0]
        self.assertTrue(instance is not None)

    def test_createInstance(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance().lijst
        validator = RelatieValidator(geldigeRelatieLijst)
        self.assertTrue(validator is not None)

    def test_afterInitValidateRelatie(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance().lijst
        validator = RelatieValidator(geldigeRelatieLijst)
        e = EnergiemeterAWV()
        a = Aftakking()
        v = Voedt
        self.assertTrue(validator.validateRelatieByURI(e, a, v))

    def test_afterInitValidateMultipleCases(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance().lijst
        validator = RelatieValidator(geldigeRelatieLijst)
        e = EnergiemeterAWV()
        a = Aftakking()
        s = Stroomkring()
        c = Contactor()
        h = Hoofdschakelaar()
        v = Voedt
        b = Bevestiging

        true_cases = [
            dict(bron=e, doel=a, relatie=v),
            dict(bron=s, doel=a, relatie=v),
            dict(bron=a, doel=h, relatie=v),
            dict(bron=s, doel=c, relatie=v)
        ]
        false_cases = [
            dict(bron=e, doel=h, relatie=v),
            dict(bron=c, doel=s, relatie=v)
        ]
        deprecated_cases = [
            dict(bron=a, doel=h, relatie=b),
        ]

        for case in true_cases:
            with self.subTest(
                    f"testing valid relation: {case['bron'].typeURI.split('#')[1]} ---{case['relatie'].typeURI.split('#')[1]}--> {case['doel'].typeURI.split('#')[1]}"):
                self.assertTrue(validator.validateRelatieByURI(case['bron'], case['doel'], case['relatie']))
        for case in false_cases:
            with self.subTest(
                    f"testing invalid relation: {case['bron'].typeURI.split('#')[1]} ---{case['relatie'].typeURI.split('#')[1]}--> {case['doel'].typeURI.split('#')[1]}"):
                self.assertFalse(validator.validateRelatieByURI(case['bron'], case['doel'], case['relatie']))
        for case in deprecated_cases:
            with self.subTest(f"testing deprecated relation: {case['bron'].typeURI.split('#')[1]} ---{case['relatie'].typeURI.split('#')[1]}--> {case['doel'].typeURI.split('#')[1]}"):
                with self.assertWarns(DeprecationWarning):
                    validator.validateRelatieByURI(case['bron'], case['doel'], case['relatie'])

    def test_afterInitValidateBadRelatieByBron(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance().lijst
        validator = RelatieValidator(geldigeRelatieLijst)
        c = Contactor()
        a = Aftakking()
        v = Voedt
        self.assertFalse(validator.validateRelatieByURI(c, a, v))

    def test_afterInitValidateBadRelatieByDoel(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance().lijst
        validator = RelatieValidator(geldigeRelatieLijst)
        e = EnergiemeterAWV()
        c = Contactor()
        v = Voedt
        self.assertFalse(validator.validateRelatieByURI(e, c, v))

    def test_afterInitValidateBadRelatieByRelatie(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance().lijst
        validator = RelatieValidator(geldigeRelatieLijst)
        e = EnergiemeterAWV()
        a = Aftakking()
        b = Bevestiging
        self.assertFalse(validator.validateRelatieByURI(e, a, b))

    def test_afterInitGetGeldigeRelatiesByBronOrDoel(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance().lijst
        validator = RelatieValidator(geldigeRelatieLijst)
        a = Aftakking()
        list = validator.getGeldigeRelatiesByBronOrDoel(a.typeURI)
        self.assertEqual(4, len(list))

    def test_afterInitGetGeldigeRelatiesOnObject(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance().lijst
        validator = RelatieValidator(geldigeRelatieLijst)
        validator.enableValidateRelatieOnRelatieInteractor()
        a = Aftakking()
        self.assertEqual(0, len(a._geldigeRelaties))
        a._loadGeldigeRelaties()
        self.assertGreater(len(a._geldigeRelaties), 0)

    def test_afterInitValidateRelatieOnObject(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance().lijst
        validator = RelatieValidator(geldigeRelatieLijst)
        validator.enableValidateRelatieOnRelatieInteractor()
        a = Aftakking()
        e = EnergiemeterAWV()
        v = Voedt
        c = Contactor()
        h = Hoofdschakelaar()
        self.assertTrue(a._validateRelatiePossible(e, v, RelatieRichting.DOEL_BRON))
        self.assertFalse(a._validateRelatiePossible(e, v, RelatieRichting.BRON_DOEL))
        self.assertFalse(a._validateRelatiePossible(c, v, RelatieRichting.DOEL_BRON))
        self.assertTrue(a._validateRelatiePossible(h, v, RelatieRichting.BRON_DOEL))

    def test_showGeldigeRelatieOnObject(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance().lijst
        validator = RelatieValidator(geldigeRelatieLijst)
        validator.enableValidateRelatieOnRelatieInteractor()
        a = Aftakking()
        result = a._showGeldigeRelaties()
        expected = """https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking  --- https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt --> https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoofdschakelaar
https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking  --- https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging --> https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoofdschakelaar
https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterAWV  --- https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt --> https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking
https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring  --- https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt --> https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking
"""
        self.assertEqual(expected, result)


class RelatieValidatorTestsUsingFacility(unittest.TestCase):
    def test_afterInitFacilityValidateRelatieOnObject(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        settings_file_location = f'{base_dir}/../settings_OTLMOW.json'
        facility = OTLFacility(logfile='', settings_path=settings_file_location, enable_relation_features=True)
        a = Aftakking()
        e = EnergiemeterAWV()
        v = Voedt
        c = Contactor()
        h = Hoofdschakelaar()
        self.assertTrue(a._validateRelatiePossible(e, v, RelatieRichting.DOEL_BRON))
        self.assertFalse(a._validateRelatiePossible(e, v, RelatieRichting.BRON_DOEL))
        self.assertFalse(a._validateRelatiePossible(c, v, RelatieRichting.DOEL_BRON))
        self.assertTrue(a._validateRelatiePossible(h, v, RelatieRichting.BRON_DOEL))


