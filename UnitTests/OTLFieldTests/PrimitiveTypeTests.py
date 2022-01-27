import unittest
from datetime import datetime, time

from src.OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from src.OTLMOW.OTLModel.Classes.Agent import Agent
from src.OTLMOW.OTLModel.Classes.HoutigeVegetatie import HoutigeVegetatie
from src.OTLMOW.OTLModel.Classes.KabelnetToegang import KabelnetToegang
from src.OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from src.OTLMOW.OTLModel.Datatypes.DateField import DateField
from src.OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMaand import KwantWrdInMaand
from src.OTLMOW.OTLModel.Datatypes.TimeField import TimeField


class TestInstance(KabelnetToegang, HoutigeVegetatie):
    def __init__(self):
        KabelnetToegang.__init__(self)
        HoutigeVegetatie.__init__(self)


class PrimitiveTypeTests(unittest.TestCase):
    def test_stringTestsTwoInstances(self):
        instance = TestInstance()
        instance2 = TestInstance()

        instance.notitie = "1"
        self.assertTrue(instance.notitie == "1")

        instance2.notitie = "2"
        self.assertTrue(instance.notitie == "1")
        self.assertTrue(instance2.notitie == "2")

    def test_BooleanFieldTests(self):
        instance = TestInstance()

        self.assertEqual(instance._isActief.field.objectUri, "http://www.w3.org/2001/XMLSchema#boolean")
        self.assertIsNone(instance.isActief)

        instance.isActief = True
        self.assertEqual(instance._isActief.field, BooleanField)
        self.assertTrue(instance.isActief)
        self.assertTrue(isinstance(instance.isActief, bool))

        instance.isActief = False
        self.assertFalse(instance.isActief)

        with self.assertRaises(CouldNotConvertToCorrectType):
            instance.isActief = "a"

    def test_IntegerFieldTests(self):
        instance = TestInstance()

        self.assertEqual("http://www.w3.org/2001/XMLSchema#integer", instance._kabelnetToegangId.field.objectUri)
        self.assertIsNone(instance.kabelnetToegangId)
        self.assertEqual(instance._kabelnetToegangId.field, IntegerField)

        instance.kabelnetToegangId = 2
        self.assertTrue(instance.kabelnetToegangId == 2)
        self.assertTrue(isinstance(instance.kabelnetToegangId, int))

        instance.kabelnetToegangId = True  # also works, True == 1 and False == 0
        self.assertTrue(instance.kabelnetToegangId == 1)

        with self.assertRaises(CouldNotConvertToCorrectType):
            instance.kabelnetToegangId = "a"

    def test_nonNegIntTests(self):
        instance = TestInstance()

        self.assertIsNone(instance.theoretischeLevensduur.waarde)
        self.assertEqual(instance._theoretischeLevensduur.field, KwantWrdInMaand)

        instance.theoretischeLevensduur.waarde = 5
        self.assertEqual(5, instance.theoretischeLevensduur.waarde)
        self.assertTrue(isinstance(instance.theoretischeLevensduur.waarde, int))

        with self.assertRaises(TypeError):
            instance.theoretischeLevensduur.waarde = "1"

        with self.assertRaises(ValueError):
            instance.theoretischeLevensduur.waarde = -1

    def test_dateTests(self):
        instance = TestInstance()

        self.assertEqual("http://www.w3.org/2001/XMLSchema#date", instance._datumOprichtingObject.field.objectUri)
        self.assertIsNone(instance.datumOprichtingObject)
        self.assertEqual(instance._datumOprichtingObject.field, DateField)

        instance.datumOprichtingObject = datetime(2021, 2, 5)
        self.assertEqual(5, instance.datumOprichtingObject.day)
        self.assertEqual(2, instance.datumOprichtingObject.month)
        self.assertEqual(2021, instance.datumOprichtingObject.year)
        self.assertTrue(isinstance(instance.datumOprichtingObject, datetime))

        self.assertEqual("2021-02-05", instance._datumOprichtingObject.field.value_default(instance.datumOprichtingObject))

    def test_timeTests(self):
        instance = Agent()

        self.assertEqual("http://www.w3.org/2001/XMLSchema#time", instance.contactinfo.beschikbaarheid._openingstijd.field.objectUri)
        self.assertIsNone(instance.contactinfo.beschikbaarheid.openingstijd)
        self.assertEqual(instance.contactinfo.beschikbaarheid._openingstijd.field, TimeField)

        instance.contactinfo.beschikbaarheid.openingstijd = time(10, 11, 12)
        self.assertEqual(10, instance.contactinfo.beschikbaarheid.openingstijd.hour)
        self.assertEqual(11, instance.contactinfo.beschikbaarheid.openingstijd.minute)
        self.assertEqual(12, instance.contactinfo.beschikbaarheid.openingstijd.second)
        self.assertTrue(isinstance(instance.contactinfo.beschikbaarheid.openingstijd, time))

        self.assertEqual("10:11:12", instance.contactinfo.beschikbaarheid._openingstijd.field.value_default(instance.contactinfo.beschikbaarheid.openingstijd))