from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from TestClasses.OTLModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass


class NonStringableObject(object):
    def __str__(self):
        pass


class FloatOrDecimalAttributeTests(TestCase):
    def test_full_test_on_testclass_kard_1(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNone(instance.testDecimalField)

        with self.subTest('assign values to DecimalNumberField with kard 1'):
            instance.testDecimalField = 1.0
            self.assertEqual(1.0, instance.testDecimalField)
            instance.testDecimalField = 2
            self.assertEqual(2, instance.testDecimalField)

    def test_full_test_on_testclass_kard_more(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNone(instance.testDecimalFieldMetKard)

        with self.subTest('assign value to DecimalNumberField with kard * by using add_value method'):
            instance._testDecimalFieldMetKard.add_value(1.0)
            self.assertEqual(1.0, instance.testDecimalFieldMetKard[0])
            instance._testDecimalFieldMetKard.add_value(2)
            self.assertEqual(1.0, instance.testDecimalFieldMetKard[0])
            self.assertEqual(2, instance.testDecimalFieldMetKard[1])

        with self.subTest('assign bad value to DecimalNumberField with kard * by using add_value method'):
            with self.assertRaises(CouldNotConvertToCorrectType):
                instance._testDecimalFieldMetKard.add_value('a')

        with self.subTest('assign value directly to DecimalNumberField with kard *'):
            instance.testDecimalNumberFieldMetKard = [1.0]
            self.assertEqual(1.0, instance.testDecimalNumberFieldMetKard[0])
            instance.testDecimalNumberFieldMetKard = [2]
            self.assertEqual(2, instance.testDecimalNumberFieldMetKard[0])
            instance.testDecimalNumberFieldMetKard = [1.0, 2]
            self.assertEqual(1.0, instance.testDecimalNumberFieldMetKard[0])
            self.assertEqual(2, instance.testDecimalNumberFieldMetKard[1])
