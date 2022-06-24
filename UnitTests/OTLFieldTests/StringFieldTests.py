import logging
from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


class NonStringableObject(object):
    def __str__(self):
        pass


class StringFieldTests(TestCase):
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
        with self.subTest('Correct values'):
            self.assertIsNone(StringField.convert_to_correct_type(None))
            self.assertEqual('a', StringField.convert_to_correct_type('a'))
            self.assertEqual('', StringField.convert_to_correct_type(''))
            self.assertEqual('1', StringField.convert_to_correct_type('1'))

        convertable_values_list = [(True, 'True'), (1.0, '1.0'), (False, 'False'), (-1, '-1'), (2.000, '2.0')]
        for value, expected in convertable_values_list:
            with self.subTest(f'Correct value after conversion: value = {value}'):
                with self.assertLogs() as captured:
                    self.assertEqual(expected, StringField.convert_to_correct_type(value))
                    warnings = list(filter(lambda r: r.levelno == logging.WARNING, list(captured.records)))
                    self.assertGreater(len(warnings), 0)

        incorrect_values = [NonStringableObject(), [], {}]
        for index, value in enumerate(incorrect_values):
            with self.subTest(f'Could not perform conversion: valueindex = {index}'):
                with self.assertRaises(CouldNotConvertToCorrectTypeError):
                    StringField.convert_to_correct_type(value)
