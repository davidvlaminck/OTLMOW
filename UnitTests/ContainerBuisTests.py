import unittest

from ModelGenerator.BaseClasses.KardinaliteitField import KardinaliteitField
from OTLClasses.Verification.ContainerBuis import ContainerBuis


class ContainerBuisInstance(ContainerBuis):
    def __init__(self):
        pass


class ContainerBuisTests(unittest.TestCase):
    def test_ContainerBuisInit(self):
        with self.assertRaises(TypeError):
            abstractInstance = ContainerBuis()
        instance = ContainerBuisInstance()
        ContainerBuis.kleur = KardinaliteitField(str, 1, 2)
        instance.kleur = None
        self.assertTrue(instance.kleur is None)

        with self.assertRaises(ValueError) as exc_array:
            instance.kleur = []
        self.assertEqual(str(exc_array.exception), "expecting tuple in KardinaliteitField")

        with self.assertRaises(ValueError) as exc_dict:
            instance.kleur = {}
        self.assertEqual(str(exc_dict.exception), "expecting tuple in KardinaliteitField")

        with self.assertRaises(ValueError) as exc_empty_tuple:
            instance.kleur = ()
        self.assertEqual(str(exc_empty_tuple.exception), "expecting at least 1 element(s) in KardinaliteitField")

        instance.kleur = ('geel',)  # tuple with one element => use a comma
        self.assertTrue(len(instance.kleur) == 1)

        instance.kleur = ("geel", "rood")
        self.assertTrue(len(instance.kleur) == 2)

        with self.assertRaises(ValueError) as exc_tuple_with_bad_value:
            instance.kleur = ("geel", 3)
        self.assertEqual(str(exc_tuple_with_bad_value.exception), "element of bad type in KardinaliteitField")

        with self.assertRaises(ValueError) as exc_tuple_with_too_many_items:
            instance.kleur = ("geel", "rood", "blauw")
        self.assertEqual(str(exc_tuple_with_too_many_items.exception), "expecting at most 2 element(s) in KardinaliteitField")

        # two instances do not share this field
        instance2 = ContainerBuisInstance()
        instance2.kleur = ("blauw",)
        self.assertTrue(instance.kleur[0] == "geel")
        self.assertTrue(instance.kleur[1] == "rood")
        self.assertTrue(instance2.kleur[0] == "blauw")
