import decimal
import unittest
from OTLClasses.Verification.Voedt import Voedt
from OTLClasses.Verification.KwantWrdInVolt import KwantWrdInVolt


class ContainerBuisTests(unittest.TestCase):
    def test_ContainerBuisInit(self):
        instance = ContainerBuis()


        # self.assertTrue(isinstance(instance.aansluitspanning, KwantWrdInVolt))
        # instance.aansluitspanning = KwantWrdInVolt(decimal.Decimal(2)) #beide werken
        # instance.aansluitspanning.waarde = decimal.Decimal(3)
        # self.assertTrue(isinstance(instance.aansluitspanning.waarde, decimal.Decimal))
        # with self.assertRaises(ValueError):
        #     instance.aansluitspanning = KwantWrdInVolt(2)
        # self.assertTrue(instance.aansluitspanning.standaardEenheid == "V")
        #
        # with self.assertRaises(AttributeError):
        #     instance.aansluitspanning.standaardEenheid = 'A'
        #
        #




