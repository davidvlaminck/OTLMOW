import unittest

from OTLMOW.OTLModel.Datatypes.KwantWrdInVolt import KwantWrdInVolt
from OTLMOW.OTLModel.Classes.Voedt import Voedt


class RelatiesTests(unittest.TestCase):
    def test_VoedtInit(self):
        instance = Voedt()

        self.assertEqual(instance._aansluitspanning.field, KwantWrdInVolt)
        self.assertEqual(None, instance.aansluitspanning.waarde)

        instance.aansluitspanning.waarde = 3.0
        self.assertEqual(3, instance.aansluitspanning.waarde)
        self.assertEqual("V", instance.aansluitspanning.standaardEenheid)

        instance.aansluitspanning .waarde = 4
        self.assertEqual(4.0, instance.aansluitspanning.waarde)

        with self.assertRaises(AttributeError):
            instance._aansluitspanning.standaardEenheid.waarde = 'A'
        with self.assertRaises(AttributeError):
            instance.aansluitspanning.standaardEenheid = 'A'


