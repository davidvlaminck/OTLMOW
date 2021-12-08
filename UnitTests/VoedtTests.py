import decimal
import unittest

from ModelGenerator.BaseClasses.DecimalField import DecimalField
from OTLClasses.Verification.Voedt import Voedt
from OTLClasses.Verification.KwantWrdInVolt import KwantWrdInVolt


class RelatiesTests(unittest.TestCase):
    def test_VoedtInit(self):
        instance = Voedt()

        self.assertTrue(isinstance(instance.aansluitspanning, KwantWrdInVolt))
        self.assertTrue(instance.aansluitspanning.standaardEenheid.waarde == "V")
        instance.aansluitspanning.waarde = decimal.Decimal(3)
        instance.aansluitspanning = KwantWrdInVolt(decimal.Decimal(3))  # beide werken

        with self.assertRaises(ValueError):
            instance.aansluitspanning = KwantWrdInVolt(2)

        with self.assertRaises(AttributeError):
            instance.aansluitspanning.standaardEenheid.waarde = 'A'

        self.assertTrue(isinstance(instance.aansluitspanning.waarde, DecimalField))


