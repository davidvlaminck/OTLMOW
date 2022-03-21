import datetime
from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
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
        self.assertIsNone(IntegerField.convert_to_correct_type(None))
        self.assertEqual(1, IntegerField.convert_to_correct_type(True))
        self.assertEqual(0, IntegerField.convert_to_correct_type(False))
        self.assertEqual(1, IntegerField.convert_to_correct_type('1'))
        self.assertEqual(1, IntegerField.convert_to_correct_type(1.0))

        with self.assertRaises(CouldNotConvertToCorrectType):
            IntegerField.convert_to_correct_type('a')
        with self.assertRaises(CouldNotConvertToCorrectType):
            IntegerField.convert_to_correct_type(object())
        with self.assertRaises(CouldNotConvertToCorrectType):
            IntegerField.convert_to_correct_type([])
        with self.assertRaises(CouldNotConvertToCorrectType):
            IntegerField.convert_to_correct_type({})
