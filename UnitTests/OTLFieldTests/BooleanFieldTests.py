import logging
from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from TestClasses.OTLModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass


class BooleanFieldTests(TestCase):
    def test_full_test_on_testclass(self):
        instance = AllCasesTestClass()
        self.assertIsNone(instance.testBooleanField)
        instance.testBooleanField = True
        self.assertTrue(instance.testBooleanField)
        instance.testBooleanField = False
        self.assertFalse(instance.testBooleanField)

    def test_validate(self):
        boolean_attribute = OTLAttribuut(naam='boolean attribuut')
        self.assertTrue(BooleanField.validate(True, boolean_attribute))
        self.assertTrue(BooleanField.validate(False, boolean_attribute))
        with self.assertRaises(TypeError):
            BooleanField.validate('a', boolean_attribute)
        with self.assertRaises(TypeError):
            BooleanField.validate([], boolean_attribute)
        with self.assertRaises(TypeError):
            BooleanField.validate(object(), boolean_attribute)
        with self.assertRaises(TypeError):
            BooleanField.validate(1, boolean_attribute)
        with self.assertRaises(TypeError):
            BooleanField.validate(1.0, boolean_attribute)

    def test_convert_to_correct_type(self):
        with self.subTest('Correct values'):
            self.assertIsNone(BooleanField.convert_to_correct_type(None))
            self.assertTrue(BooleanField.convert_to_correct_type(True))
            self.assertFalse(BooleanField.convert_to_correct_type(False))
            self.assertTrue(BooleanField.convert_to_correct_type(1))
            self.assertFalse(BooleanField.convert_to_correct_type(0))

        convertable_values_dict = {'true': True, 'True': True, 'false': False, 'False': False}
        for value, expected in convertable_values_dict.items():
            with self.subTest(f'Correct value after conversion: value = {value}'):
                with self.assertLogs() as captured:
                    self.assertEqual(expected, BooleanField.convert_to_correct_type(value))
                    warnings = list(filter(lambda r: r.levelno == logging.WARNING, list(captured.records)))
                    self.assertGreater(len(warnings), 0)

        incorrect_values = ['a', '1', 'y', 'Y', object(), [], {}]
        for value in incorrect_values:
            with self.subTest(f'Could not perform conversion: value = {value}'):
                with self.assertRaises(CouldNotConvertToCorrectTypeError):
                    BooleanField.convert_to_correct_type(value)
