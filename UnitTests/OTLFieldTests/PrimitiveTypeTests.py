import unittest
from datetime import datetime, time

from OTLModel.Classes.Agent import Agent
from OTLModel.Classes.HoutigeVegetatie import HoutigeVegetatie
from OTLModel.Classes.KabelnetToegang import KabelnetToegang
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.KwantWrdInMaand import KwantWrdInMaand
from OTLModel.Datatypes.TimeField import TimeField


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

        self.assertEquals(instance._isActief.field.objectUri, "http://www.w3.org/2001/XMLSchema#boolean")
        self.assertIsNone(instance.isActief)

        instance.isActief = True
        self.assertEquals(instance._isActief.field, BooleanField)
        self.assertTrue(instance.isActief)
        self.assertTrue(isinstance(instance.isActief, bool))

        instance.isActief = False
        self.assertFalse(instance.isActief)

        with self.assertRaises(TypeError):
            instance.isActief = "True"

        with self.assertRaises(TypeError):
            instance.isActief = 0

    def test_IntegerFieldTests(self):
        instance = TestInstance()

        self.assertEquals("http://www.w3.org/2001/XMLSchema#integer", instance._kabelnetToegangId.field.objectUri)
        self.assertIsNone(instance.kabelnetToegangId)
        self.assertEquals(instance._kabelnetToegangId.field, IntegerField)

        instance.kabelnetToegangId = 2
        self.assertTrue(instance.kabelnetToegangId == 2)
        self.assertTrue(isinstance(instance.kabelnetToegangId, int))

        instance.kabelnetToegangId = True  # also works, True == 1 and False == 0
        self.assertTrue(instance.kabelnetToegangId == 1)

        with self.assertRaises(TypeError):
            instance.kabelnetToegangId = "1"

    def test_nonNegIntTests(self):
        instance = TestInstance()

        self.assertIsNone(instance.theoretischeLevensduur)
        self.assertEquals(instance._theoretischeLevensduur.field, KwantWrdInMaand)

        instance.theoretischeLevensduur = 5
        self.assertEqual(5, instance.theoretischeLevensduur)
        self.assertTrue(isinstance(instance.theoretischeLevensduur, int))

        with self.assertRaises(TypeError):
            instance.theoretischeLevensduur = "1"

        with self.assertRaises(ValueError):
            instance.theoretischeLevensduur = -1

    def test_dateTests(self):
        instance = TestInstance()

        self.assertEquals("http://www.w3.org/2001/XMLSchema#date", instance._datumOprichtingObject.field.objectUri)
        self.assertIsNone(instance.datumOprichtingObject)
        self.assertEquals(instance._datumOprichtingObject.field, DateField)

        instance.datumOprichtingObject = datetime(2021, 2, 5)
        self.assertEqual(5, instance.datumOprichtingObject.day)
        self.assertEqual(2, instance.datumOprichtingObject.month)
        self.assertEqual(2021, instance.datumOprichtingObject.year)
        self.assertTrue(isinstance(instance.datumOprichtingObject, datetime))

        self.assertEqual("2021-02-05", instance._datumOprichtingObject.field.value_default(instance.datumOprichtingObject))

    def test_timeTests(self):
        instance = Agent()

        self.assertEquals("http://www.w3.org/2001/XMLSchema#time", instance.contactinfo.beschikbaarheid._openingstijd.field.objectUri)
        self.assertIsNone(instance.contactinfo.beschikbaarheid.openingstijd)
        self.assertEquals(instance.contactinfo.beschikbaarheid._openingstijd.field, TimeField)

        instance.contactinfo.beschikbaarheid.openingstijd = time(10, 11, 12)
        self.assertEqual(10, instance.contactinfo.beschikbaarheid.openingstijd.hour)
        self.assertEqual(11, instance.contactinfo.beschikbaarheid.openingstijd.minute)
        self.assertEqual(12, instance.contactinfo.beschikbaarheid.openingstijd.second)
        self.assertTrue(isinstance(instance.contactinfo.beschikbaarheid.openingstijd, time))

        self.assertEqual("10:11:12", instance.contactinfo.beschikbaarheid._openingstijd.field.value_default(instance.contactinfo.beschikbaarheid.openingstijd))