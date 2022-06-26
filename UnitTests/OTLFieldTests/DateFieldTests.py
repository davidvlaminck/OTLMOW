import datetime
import logging
from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField


class DateFieldTests(TestCase):
    def test_validate(self):
        date_attribute = OTLAttribuut(naam='date attribuut')
        self.assertTrue(DateField.validate(None, date_attribute))
        self.assertTrue(DateField.validate(datetime.date(2022, 1, 1), date_attribute))
        with self.assertRaises(TypeError):
            DateField.validate('a', date_attribute)
        with self.assertRaises(TypeError):
            DateField.validate('1', date_attribute)
        with self.assertRaises(TypeError):
            DateField.validate([], date_attribute)
        with self.assertRaises(TypeError):
            DateField.validate(object(), date_attribute)
        with self.assertRaises(TypeError):
            DateField.validate(1.0, date_attribute)

    def test_convert_to_correct_type(self):
        with self.subTest('Correct values'):
            self.assertIsNone(DateField.convert_to_correct_type(None))
            self.assertEqual(datetime.date(2020, 1, 1), DateField.convert_to_correct_type(datetime.date(2020, 1, 1)))

        convertable_values_list = [('2020-01-01', datetime.date(2020, 1, 1)),
                                   ('2020-1-1', datetime.date(2020, 1, 1)),
                                   ('1/1/2020', datetime.date(2020, 1, 1)),
                                   (10000000, datetime.date(1970, 4, 26)),
                                   (datetime.datetime(2020, 1, 1, 2, 2, 2), datetime.date(2020, 1, 1))]
        for value, expected in convertable_values_list:
            with self.subTest(f'Correct value after conversion: value = {value}'):
                with self.assertLogs() as captured:
                    self.assertEqual(expected, DateField.convert_to_correct_type(value))
                    warnings = list(filter(lambda r: r.levelno == logging.WARNING, list(captured.records)))
                    self.assertGreater(len(warnings), 0)

        incorrect_values = ['a', 0.1, '0.1', object(), [], {}, True, False, datetime.time(2, 2, 2)]
        for value in incorrect_values:
            with self.subTest(f'Could not perform conversion: value = {value}'):
                with self.assertRaises(CouldNotConvertToCorrectTypeError):
                    DateField.convert_to_correct_type(value)
