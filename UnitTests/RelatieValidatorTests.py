import unittest

from Facility.OTLFacility import OTLFacility
from Loggers.NoneLogger import NoneLogger
from ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie
from ModelGenerator.BaseClasses.RelatieRichting import RelatieRichting
from ModelGenerator.BaseClasses.RelatieValidator import RelatieValidator
from OTLModel.BaseClasses.RelatieInteractor import RelatieInteractor
from OTLModel.Classes.Aftakking import Aftakking
from OTLModel.Classes.Bevestiging import Bevestiging
from OTLModel.Classes.Contactor import Contactor
from OTLModel.Classes.EnergiemeterAWV import EnergiemeterAWV
from OTLModel.Classes.Hoofdschakelaar import Hoofdschakelaar
from OTLModel.Classes.RelatieObject import RelatieObject
from OTLModel.Classes.Stroomkring import Stroomkring
from OTLModel.Classes.Voedt import Voedt
from OTLModel.ClassLoader import ClassLoader


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
        classLoader = ClassLoader()

        bronClassName = UriToClassNameLijst().dict[bron]
        bronInstance = classLoader.dynamic_create_instance_from_name(bronClassName)
        if not (isinstance(bronInstance, RelatieInteractor)):
            raise TypeError("parameter bron is geen AbstractRelatieInteractor")

        doelClassName = UriToClassNameLijst().dict[doel]
        doelInstance = classLoader.dynamic_create_instance_from_name(doelClassName)
        if not (isinstance(doelInstance, RelatieInteractor)):
            raise TypeError("parameter doel is geen AbstractRelatieInteractor")

        relatieClassName = UriToClassNameLijst().dict[relatie]
        relatieInstance = classLoader.dynamic_create_instance_from_name(relatieClassName)
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
                            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt'),
            GeldigeRelatie('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring',
                            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking',
                            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt'),
            GeldigeRelatie('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking',
                            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoofdschakelaar',
                            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt'),
            GeldigeRelatie('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring',
                            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor',
                            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt')
        ]


class RelatieValidatorWithoutInstanceTests(unittest.TestCase):
    def test_beforeInitValidateRelatieOnObject(self):
        e = EnergiemeterAWV()
        a = Aftakking()
        v = Voedt
        with self.assertRaises(NotImplementedError):
            self.assertTrue(a._validateRelatiePossible(e, v, RelatieRichting.DOEL_BRON))


class RelatieValidatorTests(unittest.TestCase):
    def test_GeldigeRelatieAttrOk(self):
        instance = GeldigeRelatieLijstTestInstance().lijst[0]
        self.assertTrue(instance is not None)

    def test_createInstance(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)
        self.assertTrue(validator is not None)

    def test_createInstanceSingleton(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)
        validator.test = True
        validator2 = RelatieValidator(geldigeRelatieLijst)
        self.assertTrue(validator2.test)

    def test_afterInitValidateRelatie(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)
        e = EnergiemeterAWV()
        a = Aftakking()
        v = Voedt
        self.assertTrue(validator.validateRelatieByURI(e, a, v))

    def test_afterInitValidateMultipleRelaties(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)
        e = EnergiemeterAWV()
        a = Aftakking()
        s = Stroomkring()
        c = Contactor()
        h = Hoofdschakelaar()
        v = Voedt
        self.assertTrue(validator.validateRelatieByURI(e, a, v))
        self.assertTrue(validator.validateRelatieByURI(s, a, v))
        self.assertTrue(validator.validateRelatieByURI(a, h, v))
        self.assertTrue(validator.validateRelatieByURI(s, c, v))

    def test_afterInitValidateBadRelatieByBron(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)
        c = Contactor()
        a = Aftakking()
        v = Voedt
        self.assertFalse(validator.validateRelatieByURI(c, a, v))

    def test_afterInitValidateBadRelatieByDoel(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)
        e = EnergiemeterAWV()
        c = Contactor()
        v = Voedt
        self.assertFalse(validator.validateRelatieByURI(e, c, v))

    def test_afterInitValidateBadRelatieByRelatie(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)
        e = EnergiemeterAWV()
        a = Aftakking()
        b = Bevestiging
        self.assertFalse(validator.validateRelatieByURI(e, a, b))

    def test_afterInitGetGeldigeRelatiesByBronOrDoel(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)
        a = Aftakking()
        list = validator.getGeldigeRelatiesByBronOrDoel(a.typeURI)
        self.assertEqual(3, len(list))

    def test_afterInitGetGeldigeRelatiesOnObject(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)
        a = Aftakking()
        self.assertEqual(0, len(a._geldigeRelaties))
        a._loadGeldigeRelaties()
        self.assertGreater(len(a._geldigeRelaties), 0)

    def test_afterInitValidateRelatieOnObject(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)
        a = Aftakking()
        e = EnergiemeterAWV()
        v = Voedt
        c = Contactor()
        h = Hoofdschakelaar()
        self.assertTrue(a._validateRelatiePossible(e, v, RelatieRichting.DOEL_BRON))
        self.assertFalse(a._validateRelatiePossible(e, v, RelatieRichting.BRON_DOEL))
        self.assertFalse(a._validateRelatiePossible(c, v, RelatieRichting.DOEL_BRON))
        self.assertTrue(a._validateRelatiePossible(h, v, RelatieRichting.BRON_DOEL))

    def test_afterInitFacilityValidateRelatieOnObject(self):
        facility = OTLFacility(NoneLogger())
        a = Aftakking()
        e = EnergiemeterAWV()
        v = Voedt
        c = Contactor()
        h = Hoofdschakelaar()
        self.assertTrue(a._validateRelatiePossible(e, v, RelatieRichting.DOEL_BRON))
        self.assertFalse(a._validateRelatiePossible(e, v, RelatieRichting.BRON_DOEL))
        self.assertFalse(a._validateRelatiePossible(c, v, RelatieRichting.DOEL_BRON))
        self.assertTrue(a._validateRelatiePossible(h, v, RelatieRichting.BRON_DOEL))
