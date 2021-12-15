import decimal
import unittest

from OTLModel.Datatypes.KwantWrdInVolt import KwantWrdInVolt
from OTLModel.Datatypes.DecimalField import DecimalField
from OTLModel.Verification.Voedt import Voedt


class RelatiesTests(unittest.TestCase):
    def test_VoedtInit(self):
        instance = Voedt()

        self.assertTrue(isinstance(instance.aansluitspanning, KwantWrdInVolt))
        self.assertEqual("V", instance.aansluitspanning.eenheidVeld.waarde)
        self.assertEqual(None, instance.aansluitspanning.waarde)

        instance.aansluitspanning.waarde = decimal.Decimal(3)
        self.assertEqual(3.0, instance.aansluitspanning.waarde)

        instance.aansluitspanning = KwantWrdInVolt(decimal.Decimal(1))  # beide werken
        self.assertEqual(1.0, instance.aansluitspanning.waarde)

        with self.assertRaises(ValueError):
            instance.aansluitspanning = KwantWrdInVolt(2)

        with self.assertRaises(AttributeError):
            instance.aansluitspanning.standaardEenheid.waarde = 'A'

        self.assertTrue(isinstance(instance.aansluitspanning.waardeVeld, DecimalField))
