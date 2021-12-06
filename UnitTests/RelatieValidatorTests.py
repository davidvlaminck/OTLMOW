import unittest

from ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie
from ModelGenerator.BaseClasses.RelatieRichting import RelatieRichting
from ModelGenerator.BaseClasses.RelatieValidator import RelatieValidator
from OTLClasses.Verification.Aftakking import Aftakking
from OTLClasses.Verification.Bevestiging import Bevestiging
from OTLClasses.Verification.Contactor import Contactor
from OTLClasses.Verification.EnergiemeterAWV import EnergiemeterAWV
from OTLClasses.Verification.GeldigeRelatieLijst import GeldigeRelatieLijst
from OTLClasses.Verification.Hoofdschakelaar import Hoofdschakelaar
from OTLClasses.Verification.Stroomkring import Stroomkring
from OTLClasses.Verification.Voedt import Voedt


class GeldigeRelatieLijstTestInstance(GeldigeRelatieLijst):
    def __init__(self):
        GeldigeRelatieLijst.__init__(self)
        self.lijst = [
            GeldigeRelatie(EnergiemeterAWV, Aftakking, Voedt),
            GeldigeRelatie(Stroomkring, Aftakking, Voedt),
            GeldigeRelatie(Aftakking, Hoofdschakelaar, Voedt),
            GeldigeRelatie(Stroomkring, Contactor, Voedt),
        ]

class RelatieValidatorTests(unittest.TestCase):
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
        self.assertTrue(validator.validateRelatie(e, a, v))

    def test_afterInitValidateMultipleRelaties(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)
        e = EnergiemeterAWV()
        a = Aftakking()
        s = Stroomkring()
        c = Contactor()
        h = Hoofdschakelaar()
        v = Voedt
        self.assertTrue(validator.validateRelatie(e, a, v))
        self.assertTrue(validator.validateRelatie(s, a, v))
        self.assertTrue(validator.validateRelatie(a, h, v))
        self.assertTrue(validator.validateRelatie(s, c, v))

    def test_afterInitValidateBadRelatieByBron(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)
        c = Contactor()
        a = Aftakking()
        v = Voedt
        self.assertFalse(validator.validateRelatie(c, a, v))

    def test_afterInitValidateBadRelatieByDoel(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)
        e = EnergiemeterAWV()
        c = Contactor()
        v = Voedt
        self.assertFalse(validator.validateRelatie(e, c, v))

    def test_afterInitValidateBadRelatieByRelatie(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)
        e = EnergiemeterAWV()
        a = Aftakking()
        b = Bevestiging
        self.assertFalse(validator.validateRelatie(e, a, b))

    def test_afterInitGetGeldigeRelatiesByBronOrDoel(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)
        a = Aftakking()
        list = validator.getGeldigeRelatiesByBronOrDoel(a)
        self.assertTrue(len(list) == 3)

    def test_afterInitGetGeldigeRelatiesOnObject(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)
        a = Aftakking()
        self.assertTrue(len(a._geldigeRelaties) > 0)

    def test_afterInitValidateRelatieOnObject(self):
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)
        e = EnergiemeterAWV()
        a = Aftakking()
        v = Voedt
        c = Contactor()
        h = Hoofdschakelaar()
        self.assertTrue(a.validateRelatiePossible(e, v, RelatieRichting.DOEL_BRON))
        self.assertFalse(a.validateRelatiePossible(e, v, RelatieRichting.BRON_DOEL))
        self.assertFalse(a.validateRelatiePossible(c, v, RelatieRichting.DOEL_BRON))
        self.assertTrue(a.validateRelatiePossible(h, v, RelatieRichting.BRON_DOEL))

    def test_afterInitValidateRelatieOnObject(self):
        e = EnergiemeterAWV()
        a = Aftakking()
        v = Voedt
        with self.assertRaises(NotImplementedError):
            self.assertTrue(a.validateRelatiePossible(e, v, RelatieRichting.DOEL_BRON))