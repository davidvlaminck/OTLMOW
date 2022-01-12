import unittest

from OTLModel.Classes.Buis import Buis
from OTLModel.Classes.ContainerBuis import ContainerBuis
from OTLModel.Classes.Mantelbuis import Mantelbuis


class ContainerBuisKardinaliteitFieldTests(unittest.TestCase):
    def test_alternatives_set_and_get_waarde_KardinaliteitField(self):
        mantelbuis = Mantelbuis()
        mantelbuis.kleur.set_waarde_by_index('rood', 1)
        mantelbuis.kleur.set_waarde_by_index('geel', 0)

        # default
        self.assertEqual("geel", mantelbuis.kleur.waarde[0].waarde)
        self.assertEqual("rood", mantelbuis.kleur.waarde[1].waarde)
        # alternative 1
        self.assertEqual("geel", mantelbuis.kleur.waarde_index(0))
        self.assertEqual("rood", mantelbuis.kleur.waarde_index(1))
        # alternative 2
        kleurwaardes = mantelbuis.kleur.volgende_waarde()
        self.assertEqual("geel", next(kleurwaardes))
        self.assertEqual("rood", next(kleurwaardes))


    def test_ContainerBuisPassTests(self):
        instance = Mantelbuis()

        instance.kleur.waarde = ['geel']
        self.assertTrue(len(instance.kleur.waarde) == 1)
        self.assertEqual("geel", instance.kleur.waarde[0].waarde)

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

        with self.assertRaises(ValueError) as exc_tuple_with_bad_value:
            instance.kleur.waarde = ["geel", 3]
        self.assertEqual(str(exc_tuple_with_bad_value.exception), "element of bad type in kleur.waarde")

        instance.kleur.maxKardinaliteit = 2
        instance.kleur.minKardinaliteit = 2
        with self.assertRaises(ValueError) as exc_list_one_short:
            instance.kleur.waarde = ["geel"]
        self.assertEqual(str(exc_list_one_short.exception), "expecting at least 2 element(s) in kleur.waarde")
        with self.assertRaises(ValueError) as exc_list_one_too_many:
            instance.kleur.waarde = ["geel", "rood", "blauw"]
        self.assertEqual(str(exc_list_one_too_many.exception), "expecting at most 2 element(s) in kleur.waarde")

    def test_ContainerBuisTwoInstances(self):
        instance = Mantelbuis()
        instance.kleur.waarde = ["geel", "rood"]
        instance2 = Mantelbuis()
        instance2.kleur.waarde = ["blauw"]
        self.assertTrue(instance.kleur.waarde[0].waarde == "geel")
        self.assertTrue(instance.kleur.waarde[1].waarde == "rood")
        self.assertTrue(instance2.kleur.waarde[0].waarde == "blauw")
