import decimal
import logging
from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField


class FloatOrDecimalFieldTests(TestCase):
    def test_validate(self):
        float_attribute = OTLAttribuut(naam='float attribuut')
        self.assertTrue(FloatOrDecimalField.validate(1.0, float_attribute))
        with self.assertRaises(TypeError):
            FloatOrDecimalField.validate(1, float_attribute)
        with self.assertRaises(TypeError):
            FloatOrDecimalField.validate('a', float_attribute)
        with self.assertRaises(TypeError):
            FloatOrDecimalField.validate('1', float_attribute)
        with self.assertRaises(TypeError):
            FloatOrDecimalField.validate([], float_attribute)
        with self.assertRaises(TypeError):
            FloatOrDecimalField.validate(object(), float_attribute)

    def test_convert_to_correct_type(self):
        with self.subTest('Correct values'):
            self.assertIsNone(FloatOrDecimalField.convert_to_correct_type(None))
            self.assertEqual(1, FloatOrDecimalField.convert_to_correct_type(1.0))
            self.assertEqual(-2, FloatOrDecimalField.convert_to_correct_type(-2))
            self.assertEqual(1.0, FloatOrDecimalField.convert_to_correct_type(decimal.Decimal(1)))
            self.assertEqual(-2.345, FloatOrDecimalField.convert_to_correct_type(-2.345))

        convertable_values_list = [(True, 1.0), (False, 0.0), ('-1', -1.0), ('2.0000', 2.0)]
        for value, expected in convertable_values_list:
            with self.subTest(f'Correct value after conversion: value = {value}'):
                with self.assertLogs() as captured:
                    self.assertEqual(expected, FloatOrDecimalField.convert_to_correct_type(value))
                    warnings = list(filter(lambda r: r.levelno == logging.WARNING, list(captured.records)))
                    self.assertGreater(len(warnings), 0)

        incorrect_values = ['a', object(), [], {}]
        for value in incorrect_values:
            with self.subTest(f'Could not perform conversion: value = {value}'):
                with self.assertRaises(CouldNotConvertToCorrectTypeError):
                    FloatOrDecimalField.convert_to_correct_type(value)
