import unittest
from datetime import datetime, time

from OTLModel.BaseClasses.WKTField import WKTField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.DateTimeField import DateTimeField
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField
from OTLModel.Datatypes.OTLField import OTLField
from OTLModel.Datatypes.StringField import StringField
from OTLModel.Datatypes.TimeField import TimeField


class TestInstance:
    def __init__(self):
        self.boolean = BooleanField(naam="booleanField", label="booleanField", objectUri="booleanField",
                                    definition="definitie booleanField", constraints="", usagenote="", deprecated_version="")
        """doc for boolean"""

        self.string = StringField(naam="StringField", label="StringFieldLabel", objectUri="StringFieldUri",
                                  definition="definitie StringField", constraints="", usagenote="", deprecated_version="")
        """doc for string"""

        self.int = IntegerField(naam="IntegerField", label="IntegerField", objectUri="IntegerField", definition="definitie IntegerField", constraints="",
                                usagenote="", deprecated_version="")
        """doc for int"""

        self.nonNegInt = NonNegIntegerField(naam="NonNegIntegerField", label="NonNegIntegerField", objectUri="NonNegIntegerField",
                                            definition="definitie NonNegIntegerField", constraints="", usagenote="",
                                            deprecated_version="")
        """doc for nonNegInt"""

        self.date = DateField(naam="DateField", label="DateField", objectUri="DateField",
                              definition="definitie DateField", constraints="", usagenote="",
                              deprecated_version="")
        """doc for date"""

        self.datetime = DateTimeField(naam="DateTimeField", label="DateTimeField", objectUri="DateTimeField",
                                      definition="definitie DateTimeField", constraints="", usagenote="",
                                      deprecated_version="")
        """doc for datetime"""

        self.literal = LiteralField(naam="LiteralField", label="LiteralField", objectUri="LiteralField",
                                    definition="definitie LiteralField", constraints="", usagenote="",
                                    deprecated_version="", readonlyValue="eenheid")
        """doc for literal"""

        self.time = TimeField(naam="TimeField", label="TimeField", objectUri="TimeField",
                              definition="definitie TimeField", constraints="", usagenote="",
                              deprecated_version="")
        """doc for time"""

        self.wkt = WKTField(naam="WKTField", label="WKTField", objectUri="WKTField",
                            definition="definitie WKTField", constraints="", usagenote="",
                            deprecated_version="")
        """doc for wkt """


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
        self.assertTrue(instance.string.objectUri == "StringFieldUri")
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

        self.assertTrue(instance.boolean.objectUri == "booleanField")
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

        self.assertTrue(instance.int.objectUri == "IntegerField")
        self.assertIsNone(instance.int.waarde)
        self.assertTrue(isinstance(instance.int, IntegerField))
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

        self.assertTrue(instance.nonNegInt.objectUri == "NonNegIntegerField")
        self.assertIsNone(instance.nonNegInt.waarde)
        self.assertTrue(isinstance(instance.nonNegInt, IntegerField))
        self.assertTrue(isinstance(instance.nonNegInt, OTLField))

        instance.nonNegInt.waarde = 1
        self.assertEqual(1, instance.nonNegInt.waarde)
        self.assertTrue(isinstance(instance.nonNegInt.waarde, int))

        with self.assertRaises(ValueError):
            instance.nonNegInt.waarde = -1
        with self.assertRaises(ValueError):
            instance.nonNegInt.waarde = "1"
        with self.assertRaises(ValueError):
            instance.nonNegInt.waarde = True

    def test_dateTests(self):
        instance = TestInstance()

        self.assertTrue(instance.date.objectUri == "DateField")
        self.assertIsNone(instance.date.waarde)
        self.assertTrue(isinstance(instance.date, DateField))
        self.assertTrue(isinstance(instance.date, OTLField))

        instance.date.waarde = datetime(2021, 2, 5)
        self.assertEqual(5, instance.date.waarde.day)
        self.assertEqual(2, instance.date.waarde.month)
        self.assertEqual(2021, instance.date.waarde.year)
        self.assertTrue(isinstance(instance.date.waarde, datetime))
        self.assertEqual("2021-02-05", instance.date.default())

    def test_datetimeTests(self):
        instance = TestInstance()

        self.assertTrue(instance.datetime.objectUri == "DateTimeField")
        self.assertIsNone(instance.datetime.waarde)
        self.assertTrue(isinstance(instance.datetime, DateTimeField))
        self.assertTrue(isinstance(instance.datetime, OTLField))

        instance.datetime.waarde = datetime(2021, 2, 5, 10, 11, 12)
        self.assertEqual(5, instance.datetime.waarde.day)
        self.assertEqual(2, instance.datetime.waarde.month)
        self.assertEqual(2021, instance.datetime.waarde.year)
        self.assertEqual(10, instance.datetime.waarde.hour)
        self.assertEqual(11, instance.datetime.waarde.minute)
        self.assertEqual(12, instance.datetime.waarde.second)
        self.assertTrue(isinstance(instance.datetime.waarde, datetime))
        self.assertEqual("2021-02-05 10:11:12", instance.datetime.default())

    def test_literalTests(self):
        instance = TestInstance()

        self.assertTrue(instance.literal.objectUri == "LiteralField")
        self.assertIsNotNone(instance.literal.waarde)
        self.assertTrue(isinstance(instance.literal, LiteralField))
        self.assertTrue(isinstance(instance.literal, OTLField))

        self.assertEqual("eenheid", instance.literal.waarde)
        self.assertTrue(isinstance(instance.literal.waarde, str))

        with self.assertRaises(AttributeError):
            instance.literal.waarde = "andere eenheid"

    def test_timeTests(self):
        instance = TestInstance()

        self.assertTrue(instance.time.objectUri == "TimeField")
        self.assertIsNone(instance.time.waarde)
        self.assertTrue(isinstance(instance.time, TimeField))
        self.assertTrue(isinstance(instance.time, OTLField))

        instance.time.waarde = time(10, 11, 12)
        self.assertEqual(10, instance.time.waarde.hour)
        self.assertEqual(11, instance.time.waarde.minute)
        self.assertEqual(12, instance.time.waarde.second)
        self.assertTrue(isinstance(instance.time.waarde, time))
        self.assertEqual("10:11:12", instance.time.default())

    def test_wktTests(self):
        instance = TestInstance()

        self.assertTrue(instance.wkt.objectUri == "WKTField")
        self.assertIsNone(instance.wkt.waarde)
        self.assertTrue(isinstance(instance.wkt, WKTField))
        self.assertTrue(isinstance(instance.wkt, OTLField))

        with self.assertRaises(ValueError):
            instance.wkt.waarde = 2

        with self.assertRaises(ValueError):
            instance.wkt.waarde = "invalid wkt string"
