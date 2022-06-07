from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
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
        self.assertIsNone(StringField.convert_to_correct_type(None))
        self.assertEqual('True', StringField.convert_to_correct_type(True))
        self.assertEqual('False', StringField.convert_to_correct_type(False))
        self.assertEqual('1', StringField.convert_to_correct_type(1))
        self.assertEqual('1.0', StringField.convert_to_correct_type(1.0))

        with self.assertRaises(CouldNotConvertToCorrectType):
            StringField.convert_to_correct_type(NonStringableObject())
