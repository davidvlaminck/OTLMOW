import logging
from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from OTLMOW.OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField


class NonNegIntegerFieldTests(TestCase):
    def test_validate(self):
        non_neg_integer_attribute = OTLAttribuut(naam='non neg integer attribuut')
        self.assertTrue(NonNegIntegerField.validate(0, non_neg_integer_attribute))
        self.assertTrue(NonNegIntegerField.validate(1, non_neg_integer_attribute))
        with self.assertRaises(ValueError):
            NonNegIntegerField.validate(-1, non_neg_integer_attribute)
        with self.assertRaises(TypeError):
            NonNegIntegerField.validate('a', non_neg_integer_attribute)
        with self.assertRaises(TypeError):
            NonNegIntegerField.validate('1', non_neg_integer_attribute)
        with self.assertRaises(TypeError):
            NonNegIntegerField.validate([], non_neg_integer_attribute)
        with self.assertRaises(TypeError):
            NonNegIntegerField.validate(object(), non_neg_integer_attribute)
        with self.assertRaises(TypeError):
            NonNegIntegerField.validate(1.0, non_neg_integer_attribute)

    def test_convert_to_correct_type(self):
        with self.subTest('Correct values'):
            self.assertIsNone(NonNegIntegerField.convert_to_correct_type(None))
            self.assertEqual(0, NonNegIntegerField.convert_to_correct_type(0))
            self.assertEqual(1, NonNegIntegerField.convert_to_correct_type(1))

        convertable_values_list = [(True, 1), (1.0, 1), (False, 0), ('2.0000', 2)]
        for value, expected in convertable_values_list:
            with self.subTest(f'Correct value after conversion: value = {value}'):
                with self.assertLogs() as captured:
                    self.assertEqual(expected, NonNegIntegerField.convert_to_correct_type(value))
                    warnings = list(filter(lambda r: r.levelno == logging.WARNING, list(captured.records)))
                    self.assertGreater(len(warnings), 0)

        incorrect_values = ['a', 0.1, '0.1', object(), [], {}]
        for value in incorrect_values:
            with self.subTest(f'Could not perform conversion: value = {value}'):
                with self.assertRaises(CouldNotConvertToCorrectTypeError):
                    NonNegIntegerField.convert_to_correct_type(value)
