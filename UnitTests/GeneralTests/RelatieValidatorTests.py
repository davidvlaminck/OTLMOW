import unittest

from OTLMOW.ModelGenerator.BaseClasses.RelationValidator import RelationValidator
from OTLMOW.OTLModel.Classes.ImplementatieElement.Derdenobject import Derdenobject
from OTLMOW.OTLModel.Classes.Onderdeel.Aftakking import Aftakking
from OTLMOW.OTLModel.Classes.Onderdeel.SluitAanOp import SluitAanOp


class RelatieValidatorTests(unittest.TestCase):
    def test_nieuwe_implementatie_relaties(self):
        validator = RelationValidator()
        a = Aftakking()
        d = Derdenobject()
        s = SluitAanOp()

        self.assertTrue(validator.is_valid_relation(a, s, d))
        self.assertTrue(validator.is_valid_relation(d, s, a))
