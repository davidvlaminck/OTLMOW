import unittest

from OTLModel.Classes.Buis import Buis
from OTLModel.Classes.ContainerBuis import ContainerBuis
from OTLModel.Classes.Mantelbuis import Mantelbuis


class ContainerBuisInstance(ContainerBuis):
    def __init__(self):
        super(ContainerBuis, self).__init__()
        """De kleur van de coating."""


class ContainerBuisKardinaliteitFieldTests(unittest.TestCase):
    def test_ContainerBuisPassTests(self):
        instance = Mantelbuis()

        instance.kleur.waarde = ['geel']
        self.assertTrue(len(instance.kleur.waarde) == 1)

        instance.kleur.waarde = ["geel", "rood"]
        self.assertTrue(len(instance.kleur.waarde) == 2)

        instance.kleur.waarde = None
        self.assertTrue(instance.kleur.waarde is None)

    def test_ContainerBuisErrors(self):
        with self.assertRaises(TypeError) as exc_abstract:
            ContainerBuis()
        self.assertEqual(str(exc_abstract.exception), "Can't instantiate abstract class ContainerBuis with abstract method __init__")

        with self.assertRaises(TypeError) as exc_abstract:
            Buis()
        self.assertEqual(str(exc_abstract.exception), "Can't instantiate abstract class Buis with abstract method __init__")

        instance = Mantelbuis()

        with self.assertRaises(ValueError) as exc_tuple:
            instance.kleur.waarde = ()
        self.assertEqual(str(exc_tuple.exception), "expecting list in kleur.waarde")

        with self.assertRaises(ValueError) as exc_dict:
            instance.kleur.waarde = {}
        self.assertEqual(str(exc_dict.exception), "expecting list in kleur.waarde")

        with self.assertRaises(ValueError) as exc_empty_list:
            instance.kleur.waarde = []
        self.assertEqual(str(exc_empty_list.exception), "expecting at least 1 element(s) in kleur.waarde")

        with self.assertRaises(ValueError) as exc_tuple_with_bad_value:
            instance.kleur.waarde = ["geel", 3]
        self.assertEqual(str(exc_tuple_with_bad_value.exception), "element of bad type in kleur.waarde")

        instance.kleur.maxKardinaliteit = 2
        with self.assertRaises(ValueError) as exc_tuple_with_too_many_items:
            instance.kleur.waarde = ["geel", "rood", "blauw"]
        self.assertEqual(str(exc_tuple_with_too_many_items.exception), "expecting at most 2 element(s) in kleur.waarde")

    def test_ContainerBuisTwoInstances(self):
        instance = Mantelbuis()
        instance.kleur.waarde = ["geel", "rood"]
        instance2 = Mantelbuis()
        instance2.kleur.waarde = ["blauw"]
        self.assertTrue(instance.kleur.waarde[0] == "geel")
        self.assertTrue(instance.kleur.waarde[1] == "rood")
        self.assertTrue(instance2.kleur.waarde[0] == "blauw")