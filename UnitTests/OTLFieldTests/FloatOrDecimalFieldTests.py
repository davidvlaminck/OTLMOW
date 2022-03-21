import decimal
from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
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
        self.assertIsNone(FloatOrDecimalField.convert_to_correct_type(None))
        self.assertEqual(1.0, FloatOrDecimalField.convert_to_correct_type(True))
        self.assertEqual(0.0, FloatOrDecimalField.convert_to_correct_type(False))
        self.assertEqual(1.0, FloatOrDecimalField.convert_to_correct_type('1'))
        self.assertEqual(1.0, FloatOrDecimalField.convert_to_correct_type(1))
        self.assertEqual(1.0, FloatOrDecimalField.convert_to_correct_type(decimal.Decimal(1)))

        with self.assertRaises(CouldNotConvertToCorrectType):
            FloatOrDecimalField.convert_to_correct_type('a')
        with self.assertRaises(CouldNotConvertToCorrectType):
            FloatOrDecimalField.convert_to_correct_type(object())
        with self.assertRaises(CouldNotConvertToCorrectType):
            FloatOrDecimalField.convert_to_correct_type([])
        with self.assertRaises(CouldNotConvertToCorrectType):
            FloatOrDecimalField.convert_to_correct_type({})
