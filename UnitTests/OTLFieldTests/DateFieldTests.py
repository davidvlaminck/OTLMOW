import datetime
from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
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
        self.assertIsNone(DateField.convert_to_correct_type(None))
        self.assertEqual(datetime.date(2022, 1, 1), DateField.convert_to_correct_type('2022-1-1'))

        with self.assertRaises(CouldNotConvertToCorrectType):
            DateField.convert_to_correct_type(1)
        with self.assertRaises(CouldNotConvertToCorrectType):
            DateField.convert_to_correct_type('a')
        with self.assertRaises(CouldNotConvertToCorrectType):
            DateField.convert_to_correct_type(object())
        with self.assertRaises(CouldNotConvertToCorrectType):
            DateField.convert_to_correct_type([])
        with self.assertRaises(CouldNotConvertToCorrectType):
            DateField.convert_to_correct_type({})
