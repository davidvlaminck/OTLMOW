from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField


class BooleanFieldTests(TestCase):
    def test_validate(self):
        boolean_attribute = OTLAttribuut(naam='boolean attribuut')
        self.assertTrue(BooleanField.validate(True, boolean_attribute))
        self.assertTrue(BooleanField.validate(False, boolean_attribute))
        with self.assertRaises(TypeError):
            BooleanField.validate('a', boolean_attribute)
        with self.assertRaises(TypeError):
            BooleanField.validate([], boolean_attribute)
        with self.assertRaises(TypeError):
            BooleanField.validate(object(), boolean_attribute)
        with self.assertRaises(TypeError):
            BooleanField.validate(1, boolean_attribute)
        with self.assertRaises(TypeError):
            BooleanField.validate(1.0, boolean_attribute)

    def test_convert_to_correct_type(self):
        self.assertIsNone(BooleanField.convert_to_correct_type(None))
        self.assertTrue(BooleanField.convert_to_correct_type(True))
        self.assertFalse(BooleanField.convert_to_correct_type(False))
        self.assertTrue(BooleanField.convert_to_correct_type(1))
        self.assertFalse(BooleanField.convert_to_correct_type(0))
        self.assertTrue(BooleanField.convert_to_correct_type("true"))
        self.assertFalse(BooleanField.convert_to_correct_type("false"))
        self.assertTrue(BooleanField.convert_to_correct_type("True"))
        self.assertFalse(BooleanField.convert_to_correct_type("False"))

        with self.assertRaises(CouldNotConvertToCorrectType):
            BooleanField.convert_to_correct_type('a')
        with self.assertRaises(CouldNotConvertToCorrectType):
            BooleanField.convert_to_correct_type('1')
        with self.assertRaises(CouldNotConvertToCorrectType):
            BooleanField.convert_to_correct_type('y')
        with self.assertRaises(CouldNotConvertToCorrectType):
            BooleanField.convert_to_correct_type('Y')
        with self.assertRaises(CouldNotConvertToCorrectType):
            BooleanField.convert_to_correct_type(object())
        with self.assertRaises(CouldNotConvertToCorrectType):
            BooleanField.convert_to_correct_type([])
        with self.assertRaises(CouldNotConvertToCorrectType):
            BooleanField.convert_to_correct_type({})
