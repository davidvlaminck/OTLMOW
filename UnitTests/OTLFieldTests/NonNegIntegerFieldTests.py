from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from OTLMOW.OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField


class NonNegIntegerFieldTests(TestCase):
    def test_validate(self):
        non_neg_integer_attribute = OTLAttribuut(naam='non neg integer attribuut')
        self.assertTrue(NonNegIntegerField.validate(0, non_neg_integer_attribute))
        self.assertTrue(NonNegIntegerField.validate(1, non_neg_integer_attribute))
        with self.assertRaises(ValueError):
            NonNegIntegerField.validate(-1, non_neg_integer_attribute)
        with self.assertRaises(TypeError):
            NonNegIntegerField.validate('a', non_neg_integer_attribute)
        with self.assertRaises(TypeError):
            NonNegIntegerField.validate('1', non_neg_integer_attribute)
        with self.assertRaises(TypeError):
            NonNegIntegerField.validate([], non_neg_integer_attribute)
        with self.assertRaises(TypeError):
            NonNegIntegerField.validate(object(), non_neg_integer_attribute)
        with self.assertRaises(TypeError):
            NonNegIntegerField.validate(1.0, non_neg_integer_attribute)
