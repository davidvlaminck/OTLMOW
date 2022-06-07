import datetime
import logging
from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.TimeField import TimeField


class DateTimeFieldTests(TestCase):
    def test_validate(self):
        # TODO add tests for DateTime
        self.assertTrue(False)
        time_attribute = OTLAttribuut(naam='time attribuut')
        self.assertTrue(TimeField.validate(None, time_attribute))
        self.assertTrue(TimeField.validate(datetime.time(10, 11, 12), time_attribute))
        with self.assertRaises(TypeError):
            TimeField.validate('a', time_attribute)
        with self.assertRaises(TypeError):
            TimeField.validate('1', time_attribute)
        with self.assertRaises(TypeError):
            TimeField.validate([], time_attribute)
        with self.assertRaises(TypeError):
            TimeField.validate(object(), time_attribute)
        with self.assertRaises(TypeError):
            TimeField.validate(1.0, time_attribute)

    def test_convert_to_correct_type(self):
        # TODO add tests for DateTime
        self.assertTrue(False)
        with self.subTest('Correct values'):
            self.assertIsNone(TimeField.convert_to_correct_type(None))
            self.assertEqual(datetime.time(10, 11, 12), TimeField.convert_to_correct_type(datetime.time(10, 11, 12)))

        convertable_values_list = [('10:11:12', datetime.time(10, 11, 12)), ('7:8:9', datetime.time(7, 8, 9)),
                                   ('2020-1-1 10:11:12', datetime.time(10, 11, 12)), (datetime.date(1, 1, 1), datetime.time(0, 0, 0)),
                                   ('1/1/2020 10:11:12', datetime.time(10, 11, 12)), (10000, datetime.time(3, 46, 40))]
        for value, expected in convertable_values_list:
            with self.subTest(f'Correct value after conversion: value = {value}'):
                with self.assertLogs() as captured:
                    self.assertEqual(expected, TimeField.convert_to_correct_type(value))
                    warnings = list(filter(lambda r: r.levelno == logging.WARNING, list(captured.records)))
                    self.assertGreater(len(warnings), 0)

        incorrect_values = ['a', 0.1, '0.1', object(), [], {}, True, False, '24:99:00']
        for value in incorrect_values:
            with self.subTest(f'Could not perform conversion: value = {value}'):
                with self.assertRaises(CouldNotConvertToCorrectType):
                    TimeField.convert_to_correct_type(value)
