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

        with self.subTest('assign value to stringfield with kard * by using _add_value method'):
            instance._testStringFieldMetKard.add_value('1')
            self.assertEqual('1', instance.testStringFieldMetKard[0])
            instance._testStringFieldMetKard.add_value('2')
            self.assertEqual('1', instance.testStringFieldMetKard[0])
            self.assertEqual('2', instance.testStringFieldMetKard[1])

        with self.subTest('assign bad value to stringfield with kard * by using _add_value method'):
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

    def test_validate(self):
        string_attribute = OTLAttribuut(naam='string attribuut')
        self.assertTrue(StringField.validate('a', string_attribute))
        self.assertTrue(StringField.validate('', string_attribute))
        self.assertTrue(StringField.validate('abc', string_attribute))
        with self.assertRaises(TypeError):
            StringField.validate(1, string_attribute)
        with self.assertRaises(TypeError):
            StringField.validate(True, string_attribute)
        with self.assertRaises(TypeError):
            StringField.validate([], string_attribute)
        with self.assertRaises(TypeError):
            StringField.validate(object(), string_attribute)
        with self.assertRaises(TypeError):
            StringField.validate(1.0, string_attribute)

    def test_convert_to_correct_type(self):
        self.assertIsNone(StringField.convert_to_correct_type(None))
        self.assertEqual('True', StringField.convert_to_correct_type(True))
        self.assertEqual('False', StringField.convert_to_correct_type(False))
        self.assertEqual('1', StringField.convert_to_correct_type(1))
        self.assertEqual('1.0', StringField.convert_to_correct_type(1.0))

        with self.assertRaises(CouldNotConvertToCorrectType):
            StringField.convert_to_correct_type(NonStringableObject())
