import datetime
from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.TimeField import TimeField


class DateFieldTests(TestCase):
    def test_validate(self):
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
        self.assertIsNone(TimeField.convert_to_correct_type(None))
        self.assertEqual(datetime.time(10, 11, 12), TimeField.convert_to_correct_type('10:11:12'))

        with self.assertRaises(CouldNotConvertToCorrectType):
            TimeField.convert_to_correct_type('24:99:00')
        with self.assertRaises(CouldNotConvertToCorrectType):
            TimeField.convert_to_correct_type(1)
        with self.assertRaises(CouldNotConvertToCorrectType):
            TimeField.convert_to_correct_type('a')
        with self.assertRaises(CouldNotConvertToCorrectType):
            TimeField.convert_to_correct_type(object())
        with self.assertRaises(CouldNotConvertToCorrectType):
            TimeField.convert_to_correct_type([])
        with self.assertRaises(CouldNotConvertToCorrectType):
            TimeField.convert_to_correct_type({})
