import unittest
from datetime import datetime

from ModelGenerator.BaseClasses.BooleanField import BooleanField
from ModelGenerator.BaseClasses.DateField import DateField
from ModelGenerator.BaseClasses.IntField import IntField
from ModelGenerator.BaseClasses.NonNegIntField import NonNegIntField
from ModelGenerator.BaseClasses.OTLField import OTLField
from ModelGenerator.BaseClasses.StringField import StringField


class TestInstance:
    def __init__(self):
        self.boolean = BooleanField(naam="booleanField", label="booleanField", uri="booleanField",
                                    definition="definitie booleanField", constraints="", usagenote="", deprecated_version="")
        """doc for boolean"""

        self.string = StringField(naam="StringField", label="StringFieldLabel", uri="StringFieldUri",
                                  definition="definitie StringField", constraints="", usagenote="", deprecated_version="")
        """doc for string"""

        self.int = IntField(naam="IntField", label="IntField", uri="IntField", definition="definitie IntField", constraints="",
                            usagenote="", deprecated_version="")
        """doc for int"""

        self.nonNegInt = NonNegIntField(naam="NonNegIntField", label="NonNegIntField", uri="NonNegIntField",
                                        definition="definitie NonNegIntField", constraints="", usagenote="",
                                        deprecated_version="")
        """doc for nonNegInt"""

        self.date = DateField(naam="DateField", label="DateField", uri="DateField",
                            definition="definitie DateField", constraints="", usagenote="",
                            deprecated_version="")
        """doc for nonNegInt"""


class PrimitiveTypeTests(unittest.TestCase):
    def test_stringTestsTwoInstances(self):
        instance = TestInstance()
        instance2 = TestInstance()

        instance.string.waarde = "1"
        self.assertTrue(instance.string.waarde == "1")

        instance2.string.waarde = "2"
        self.assertTrue(instance.string.waarde == "1")
        self.assertTrue(instance2.string.waarde == "2")

    def test_stringTests(self):
        instance = TestInstance()
        self.assertTrue(instance.string.uri == "StringFieldUri")
        self.assertTrue(instance.string.naam == "StringField")
        self.assertIsNone(instance.string.waarde)

        with self.assertRaises(ValueError):
            instance.string.waarde = 1
        with self.assertRaises(ValueError):
            instance.string.waarde = True

        self.assertTrue(isinstance(instance.string, StringField))
        self.assertTrue(isinstance(instance.string, OTLField))

        self.assertEqual(instance.string.primitiveType.__name__, "str")
        instance.string.waarde = "str"
        self.assertTrue(instance.string.waarde == "str")
        self.assertTrue(isinstance(instance.string.waarde, str))

    def test_BooleanFieldTests(self):
        instance = TestInstance()

        self.assertTrue(instance.boolean.uri == "booleanField")
        self.assertIsNone(instance.boolean.waarde)
        self.assertTrue(isinstance(instance.boolean, BooleanField))
        self.assertTrue(isinstance(instance.boolean, OTLField))

        instance.boolean.waarde = True
        self.assertTrue(instance.boolean.waarde)
        self.assertTrue(isinstance(instance.boolean.waarde, bool))

        instance.boolean.waarde = False
        self.assertFalse(instance.boolean.waarde)

        with self.assertRaises(ValueError):
            instance.boolean.waarde = 1

    def test_intTests(self):
        instance = TestInstance()

        self.assertTrue(instance.int.uri == "IntField")
        self.assertIsNone(instance.int.waarde)
        self.assertTrue(isinstance(instance.int, IntField))
        self.assertTrue(isinstance(instance.int, OTLField))

        instance.int.waarde = 1
        self.assertTrue(instance.int.waarde == 1)
        self.assertTrue(isinstance(instance.int.waarde, int))

        with self.assertRaises(ValueError):
            instance.int.waarde = "1"
        with self.assertRaises(ValueError):
            instance.int.waarde = True

        # with self.assertRaises(SyntaxError):
        instance.int = True

    def test_nonNegIntTests(self):
        instance = TestInstance()

        self.assertTrue(instance.nonNegInt.uri == "NonNegIntField")
        self.assertIsNone(instance.nonNegInt.waarde)
        self.assertTrue(isinstance(instance.nonNegInt, IntField))
        self.assertTrue(isinstance(instance.nonNegInt, OTLField))

        instance.nonNegInt.waarde = 1
        self.assertTrue(instance.nonNegInt.waarde == 1)
        self.assertTrue(isinstance(instance.nonNegInt.waarde, int))

        with self.assertRaises(ValueError):
            instance.nonNegInt.waarde = -1
        with self.assertRaises(ValueError):
            instance.nonNegInt.waarde = "1"
        with self.assertRaises(ValueError):
            instance.nonNegInt.waarde = True

    def test_dateTests(self):
        instance = TestInstance()

        self.assertTrue(instance.date.uri == "DateField")
        self.assertIsNone(instance.date.waarde)
        self.assertTrue(isinstance(instance.date, DateField))
        self.assertTrue(isinstance(instance.date, OTLField))

        instance.date.waarde = datetime(2021, 12, 15)
        self.assertTrue(instance.date.waarde.day == 15)
        self.assertTrue(instance.date.waarde.month == 12)
        self.assertTrue(instance.date.waarde.year == 2021)
        self.assertTrue(isinstance(instance.date.waarde, datetime))
        #
        # with self.assertRaises(ValueError):
        #     instance.nonNegInt.waarde = -1
        # with self.assertRaises(ValueError):
        #     instance.nonNegInt.waarde = "1"
        # with self.assertRaises(ValueError):
        #     instance.nonNegInt.waarde = True
