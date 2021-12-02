import unittest

from OTLClasses.Verification.ContainerBuis import ContainerBuis


class ContainerBuisInstance(ContainerBuis):
    def __init__(self):
        pass


class ContainerBuisTests(unittest.TestCase):
    def test_ContainerBuisInit(self):
        with self.assertRaises(TypeError):
            abstractInstance = ContainerBuis()
        instance = ContainerBuisInstance()
        instance.kleur = []
        self.assertTrue(len(instance.kleur) == 0)
        instance.kleur = ["geel"]
        self.assertTrue(len(instance.kleur) == 1)
        instance.kleur = ["geel","rood"]
        self.assertTrue(len(instance.kleur) == 2)
        with self.assertRaises(ValueError):
            instance.kleur = [2, 3]
        instance2 = ContainerBuisInstance()
        instance2.kleur = ["blauw"]
        self.assertTrue(instance.kleur[1] == "rood")
        self.assertTrue(instance2.kleur[0] == "blauw")


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




