import unittest

from ModelGenerator.BaseClasses.BooleanField import BooleanField
from ModelGenerator.BaseClasses.IntField import IntField
from ModelGenerator.BaseClasses.StringField import StringField


class TestInstance:
    boolean = BooleanField("testuriforbool")
    integer = IntField("testuriforint")

    string = StringField("testuriforstring")
    """doc for string"""


class PrimitiveTypeTests(unittest.TestCase):
    def test_booleanTests(self):
        instance = TestInstance()

        instance.boolean = True
        self.assertTrue(instance.boolean)
        self.assertTrue(isinstance(instance.boolean, bool))
        instance.boolean = False
        self.assertFalse(instance.boolean)

        with self.assertRaises(ValueError):
            instance.boolean = 1

    def test_primitiveUriTests(self):
        instance = TestInstance()
        instance.string = ""


    def test_stringTests(self):
        instance = TestInstance()
        instance.string = ""
        self.assertTrue(instance.string == "")
        self.assertTrue(isinstance(instance.string, str))

        with self.assertRaises(ValueError):
            instance.string = 1

    def test_intTests(self):
        instance = TestInstance()
        instance.integer = 1
        self.assertTrue(instance.integer == 1)
        self.assertTrue(isinstance(instance.integer, int))

        with self.assertRaises(ValueError):
            instance.integer = "1"
