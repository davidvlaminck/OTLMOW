from unittest import TestCase

from AllCasesTestClass import AllCasesTestClass
from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


class NonStringableObject(object):
    def __str__(self):
        pass


class StringFieldTests(TestCase):
    def test_full_test_on_testclass_kard_1(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNotNone(instance.testKwantWrd)
            self.assertTrue(instance._testKwantWrd.waarde_shortcut_applicable)

        with self.subTest('assign values to kwantWrdField with kard 1'):
            instance.testKwantWrd.waarde = 1
            self.assertEqual(1.0, instance.testKwantWrd.waarde)
            self.assertEqual('V', instance.testKwantWrd.standaardEenheid)
            instance.testKwantWrd.waarde = 2
            self.assertEqual(2, instance.testKwantWrd.waarde)

    def test_full_test_on_testclass_kard_more(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNotNone(instance.testKwantWrdMetKard)
            self.assertTrue(instance._testKwantWrdMetKard.waarde_shortcut_applicable)

        with self.subTest('assign value directly to kwantWrdField with kard *'):
            instance.testKwantWrdMetKard[0].waarde = 1.0
            self.assertEqual(1, instance.testKwantWrdMetKard[0].waarde)

        with self.subTest('assign value to kwantWrdField with kard * by using add_empty_value method'):
            instance._testKwantWrdMetKard.add_empty_value()
            instance.testKwantWrdMetKard[1].waarde = 2.0
            self.assertEqual(1, instance.testKwantWrdMetKard[0].waarde)
            self.assertEqual(2, instance.testKwantWrdMetKard[1].waarde)

        with self.subTest('assign bad value to kwantWrdField with kard *'):
            with self.assertRaises(CouldNotConvertToCorrectType):
                instance.testKwantWrdMetKard[0].waarde = 'a'
