import datetime
import logging
from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField


class IntegerFieldTests(TestCase):
    def test_validate(self):
        integer_attribute = OTLAttribuut(naam='integer attribuut')
        self.assertTrue(IntegerField.validate(None, integer_attribute))
        self.assertTrue(IntegerField.validate(0, integer_attribute))
        self.assertTrue(IntegerField.validate(1, integer_attribute))
        self.assertTrue(IntegerField.validate(-1, integer_attribute))
        with self.assertRaises(TypeError):
            IntegerField.validate('a', integer_attribute)
        with self.assertRaises(TypeError):
            IntegerField.validate('1', integer_attribute)
        with self.assertRaises(TypeError):
            IntegerField.validate([], integer_attribute)
        with self.assertRaises(TypeError):
            IntegerField.validate(object(), integer_attribute)
        with self.assertRaises(TypeError):
            IntegerField.validate(1.0, integer_attribute)

    def test_convert_to_correct_type(self):
        with self.subTest('Correct values'):
            self.assertIsNone(IntegerField.convert_to_correct_type(None))
            self.assertEqual(1, IntegerField.convert_to_correct_type(1))
            self.assertEqual(-2, IntegerField.convert_to_correct_type(-2))

        convertable_values_list = [(True, 1), (1.0, 1), (False, 0), ('-1', -1), ('2.0000', 2)]
        for value, expected in convertable_values_list:
            with self.subTest(f'Correct value after conversion: value = {value}'):
                with self.assertLogs() as captured:
                    self.assertEqual(expected, IntegerField.convert_to_correct_type(value))
                    warnings = list(filter(lambda r: r.levelno == logging.WARNING, list(captured.records)))
                    self.assertGreater(len(warnings), 0)

        incorrect_values = ['a', 0.1, '0.1', object(), [], {}]
        for value in incorrect_values:
            with self.subTest(f'Could not perform conversion: value = {value}'):
                with self.assertRaises(CouldNotConvertToCorrectTypeError):
                    IntegerField.convert_to_correct_type(value)
