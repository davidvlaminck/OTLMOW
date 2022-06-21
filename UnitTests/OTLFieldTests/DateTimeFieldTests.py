import datetime
import logging
from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.DateTimeField import DateTimeField
from OTLMOW.OTLModel.Datatypes.TimeField import TimeField


class DateTimeFieldTests(TestCase):
    def test_validate(self):
        datetime_attribute = OTLAttribuut(naam='datetime attribuut')
        self.assertTrue(DateTimeField.validate(None, datetime_attribute))
        self.assertTrue(DateTimeField.validate(datetime.datetime(2022, 2, 2, 10, 11, 12), datetime_attribute))
        with self.assertRaises(TypeError):
            TimeField.validate('a', datetime_attribute)
        with self.assertRaises(TypeError):
            TimeField.validate('1', datetime_attribute)
        with self.assertRaises(TypeError):
            TimeField.validate([], datetime_attribute)
        with self.assertRaises(TypeError):
            TimeField.validate(object(), datetime_attribute)
        with self.assertRaises(TypeError):
            TimeField.validate(1.0, datetime_attribute)

    def test_convert_to_correct_type(self):
        with self.subTest('Correct values'):
            self.assertIsNone(DateTimeField.convert_to_correct_type(None))
            self.assertEqual(datetime.datetime(2022, 2, 2, 10, 11, 12),
                             DateTimeField.convert_to_correct_type(datetime.datetime(2022, 2, 2, 10, 11, 12)))

        convertable_values_list = [('2020-2-2 10:11:12', datetime.datetime(2020, 2, 2, 10, 11, 12)),
                                   ('2/2/2020 10:11:12', datetime.datetime(2020, 2, 2, 10, 11, 12)),
                                   (datetime.date(2020, 2, 2), datetime.datetime(2020, 2, 2, 0, 0, 0)),
                                   (10000000, datetime.datetime(1970, 4, 26, 19, 46, 40))]
        for value, expected in convertable_values_list:
            with self.subTest(f'Correct value after conversion: value = {value}'):
                with self.assertLogs() as captured:
                    self.assertEqual(expected, DateTimeField.convert_to_correct_type(value))
                    warnings = list(filter(lambda r: r.levelno == logging.WARNING, list(captured.records)))
                    self.assertGreater(len(warnings), 0)

        incorrect_values = ['a', 0.1, '0.1', object(), [], {}, True, False, '24:99:00']
        for value in incorrect_values:
            with self.subTest(f'Could not perform conversion: value = {value}'):
                with self.assertRaises(CouldNotConvertToCorrectTypeError):
                    DateTimeField.convert_to_correct_type(value)
