import unittest

from OTLModel.Datatypes.KwantWrdInVolt import KwantWrdInVolt
from OTLModel.Classes.Voedt import Voedt


class RelatiesTests(unittest.TestCase):
    def test_VoedtInit(self):
        instance = Voedt()

        self.assertEqual(instance._aansluitspanning.field, KwantWrdInVolt)
        self.assertEqual("V", instance._aansluitspanning.field.eenheid.standaardEenheid)
        self.assertEqual(None, instance.aansluitspanning)

        instance.aansluitspanning = 3.0
        self.assertEqual(3, instance.aansluitspanning)

        instance.aansluitspanning = 4
        self.assertEqual(4.0, instance.aansluitspanning)

        with self.assertRaises(AttributeError):
            instance._aansluitspanning.field.eenheid.standaardEenheid = 'A'


