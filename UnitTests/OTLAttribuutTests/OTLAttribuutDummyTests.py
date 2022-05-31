from datetime import date, datetime, time
from unittest import TestCase

from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.DateTimeField import DateTimeField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KlAIMToestand import KlAIMToestand
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.OTLModel.Datatypes.TimeField import TimeField


class OTLAttribuutDummyTests(TestCase):
    def test_StringField(self):
        attr = OTLAttribuut(field=StringField)
        attr.fill_with_dummy_data()

        self.assertIsNotNone(attr.get_waarde())
        self.assertTrue(isinstance(attr.get_waarde(), str))

    def test_FloatOrDecimalField(self):
        attr = OTLAttribuut(field=FloatOrDecimalField)
        attr.fill_with_dummy_data()

        self.assertIsNotNone(attr.get_waarde())
        self.assertTrue(isinstance(attr.get_waarde(), float))

    def test_IntegerField(self):
        attr = OTLAttribuut(field=IntegerField)
        attr.fill_with_dummy_data()

        self.assertIsNotNone(attr.get_waarde())
        self.assertTrue(isinstance(attr.get_waarde(), int))

    def test_BooleanField(self):
        attr = OTLAttribuut(field=BooleanField)
        attr.fill_with_dummy_data()

        self.assertIsNotNone(attr.get_waarde())
        self.assertTrue(attr.get_waarde() == False or attr.get_waarde() == True)

    def test_DateField(self):
        attr = OTLAttribuut(field=DateField)
        attr.fill_with_dummy_data()

        self.assertIsNotNone(attr.get_waarde())
        self.assertTrue(isinstance(attr.get_waarde(), date))

    def test_DateTimeField(self):
        attr = OTLAttribuut(field=DateTimeField)
        attr.fill_with_dummy_data()

        self.assertIsNotNone(attr.get_waarde())
        self.assertTrue(isinstance(attr.get_waarde(), datetime))

    def test_TimeField(self):
        attr = OTLAttribuut(field=TimeField)
        attr.fill_with_dummy_data()

        self.assertIsNotNone(attr.get_waarde())
        self.assertTrue(isinstance(attr.get_waarde(), time))

    def test_KeuzelijstField(self):
        attr = OTLAttribuut(field=KlAIMToestand)
        attr.fill_with_dummy_data()

        self.assertIsNotNone(attr.get_waarde())
        self.assertTrue(isinstance(attr.get_waarde(), str))
