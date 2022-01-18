import unittest

from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Classes.Buis import Buis
from OTLModel.Classes.ContainerBuis import ContainerBuis
from OTLModel.Classes.Mantelbuis import Mantelbuis


class ContainerBuisKardinaliteitFieldTests(unittest.TestCase):
    def test_Mantelbuis_assign_correct_value(self):
        mantelbuis = Mantelbuis()
        mantelbuis.kleur = ['geel', 'rood']

        self.assertEqual("geel", mantelbuis.kleur[0])
        self.assertEqual("rood", mantelbuis.kleur[1])

    def test_Mantelbuis_reassign_values(self):
        mantelbuis = Mantelbuis()
        mantelbuis.kleur = ['geel']

        self.assertEqual("geel", mantelbuis.kleur[0])
        self.assertEqual(1, len(mantelbuis.kleur))

        mantelbuis.kleur = ['geel', 'rood']
        self.assertEqual(2, len(mantelbuis.kleur))

        mantelbuis.kleur = None
        self.assertIsNone(mantelbuis.kleur)

    def test_Mantelbuis_errors(self):
        with self.assertRaises(TypeError) as exc_abstract:
            ContainerBuis()
        self.assertEqual(str(exc_abstract.exception), "Can't instantiate abstract class ContainerBuis with abstract method __init__")

        with self.assertRaises(TypeError) as exc_abstract:
            Buis()
        self.assertEqual(str(exc_abstract.exception), "Can't instantiate abstract class Buis with abstract method __init__")

        instance = Mantelbuis()

        with self.assertRaises(TypeError) as exc_dict:
            instance.kleur = 2

        with self.assertRaises(TypeError) as exc_dict:
            instance.kleur = {}
        self.assertEqual(str(exc_dict.exception), "expecting a list in Mantelbuis.kleur")

        with self.assertRaises(ValueError) as exc_tuple_with_bad_value:
            instance.kleur = ["geel", 3]
        self.assertEqual(str(exc_tuple_with_bad_value.exception), "invalid value in list for Mantelbuis.kleur: 3 is not valid, must be valid for String\nexpecting string in kleur")

        instance._kleur.kardinaliteit_min = "2"
        instance._kleur.kardinaliteit_max = "2"
        with self.assertRaises(ValueError) as exc_list_one_short:
            instance.kleur = ["geel"]
        self.assertEqual(str(exc_list_one_short.exception), "expecting at least 2 element(s) in Mantelbuis.kleur")
        with self.assertRaises(ValueError) as exc_list_one_too_many:
            instance.kleur = ["geel", "rood", "blauw"]
        self.assertEqual(str(exc_list_one_too_many.exception), "expecting at most 2 element(s) in Mantelbuis.kleur")

    def test_MantelbuisTwoInstances(self):
        instance = Mantelbuis()
        instance.kleur = ["geel", "rood"]
        instance2 = Mantelbuis()
        instance2.kleur = ["blauw"]
        self.assertTrue(instance.kleur[0] == "geel")
        self.assertTrue(instance.kleur[1] == "rood")
        self.assertTrue(instance2.kleur[0] == "blauw")
