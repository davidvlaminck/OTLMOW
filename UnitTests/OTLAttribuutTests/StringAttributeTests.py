from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from TestClasses.OTLModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass


class NonStringableObject(object):
    def __str__(self):
        pass


class StringAttributeTests(TestCase):
    def test_full_test_on_testclass_kard_1(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNone(instance.testStringField)

        with self.subTest('assign values to stringfield with kard 1'):
            instance.testStringField = '1'
            self.assertEqual('1', instance.testStringField)
            instance.testStringField = '2'
            self.assertEqual('2', instance.testStringField)

    def test_full_test_on_testclass_kard_more(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNone(instance.testStringFieldMetKard)

        with self.subTest('assign value to stringfield with kard * by using add_value method'):
            instance._testStringFieldMetKard.add_value('1')
            self.assertEqual('1', instance.testStringFieldMetKard[0])
            instance._testStringFieldMetKard.add_value('2')
            self.assertEqual('1', instance.testStringFieldMetKard[0])
            self.assertEqual('2', instance.testStringFieldMetKard[1])

        with self.subTest('assign bad value to stringfield with kard * by using add_value method'):
            with self.assertRaises(CouldNotConvertToCorrectType):
                instance._testStringFieldMetKard.add_value(NonStringableObject())

        with self.subTest('assign value directly to stringfield with kard *'):
            instance.testStringFieldMetKard = ['1']
            self.assertEqual('1', instance.testStringFieldMetKard[0])
            instance.testStringFieldMetKard = ['2']
            self.assertEqual('2', instance.testStringFieldMetKard[0])
            instance.testStringFieldMetKard = ['1', '2']
            self.assertEqual('1', instance.testStringFieldMetKard[0])
            self.assertEqual('2', instance.testStringFieldMetKard[1])
