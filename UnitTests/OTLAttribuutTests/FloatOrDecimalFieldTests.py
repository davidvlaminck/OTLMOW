from unittest import TestCase

from AllCasesTestClass import AllCasesTestClass
from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


class NonStringableObject(object):
    def __str__(self):
        pass


class FloatOrDecimalTests(TestCase):
    def test_full_test_on_testclass_kard_1(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNone(instance.testDecimalNumberField)

        with self.subTest('assign values to DecimalNumberField with kard 1'):
            instance.testDecimalNumberField = 1.0
            self.assertEqual(1.0, instance.testDecimalNumberField)
            instance.testDecimalNumberField = 2
            self.assertEqual(2, instance.testDecimalNumberField)

    def test_full_test_on_testclass_kard_more(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNone(instance.testDecimalNumberFieldMetKard)

        with self.subTest('assign value to DecimalNumberField with kard * by using add_value method'):
            instance._testDecimalNumberFieldMetKard.add_value(1.0)
            self.assertEqual(1.0, instance.testDecimalNumberFieldMetKard[0])
            instance._testDecimalNumberFieldMetKard.add_value(2)
            self.assertEqual(1.0, instance.testDecimalNumberFieldMetKard[0])
            self.assertEqual(2, instance.testDecimalNumberFieldMetKard[1])

        with self.subTest('assign bad value to DecimalNumberField with kard * by using add_value method'):
            with self.assertRaises(CouldNotConvertToCorrectType):
                instance._testDecimalNumberFieldMetKard.add_value('a')

        with self.subTest('assign value directly to DecimalNumberField with kard *'):
            instance.testDecimalNumberFieldMetKard = [1.0]
            self.assertEqual(1.0, instance.testDecimalNumberFieldMetKard[0])
            instance.testDecimalNumberFieldMetKard = [2]
            self.assertEqual(2, instance.testDecimalNumberFieldMetKard[0])
            instance.testDecimalNumberFieldMetKard = [1.0, 2]
            self.assertEqual(1.0, instance.testDecimalNumberFieldMetKard[0])
            self.assertEqual(2, instance.testDecimalNumberFieldMetKard[1])
