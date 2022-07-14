from datetime import date, datetime, time
from unittest import TestCase

from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.DateTimeField import DateTimeField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.OTLModel.Datatypes.TimeField import TimeField
from TestClasses.OTLModel.Datatypes.DtuTestUnionType import DtuTestUnionType
from UnitTests.TestClasses.OTLModel.Datatypes.DtcTestComplexType import DtcTestComplexType
from UnitTests.TestClasses.OTLModel.Datatypes.KwantWrdTest import KwantWrdTest
from UnitTests.TestClasses.OTLModel.Datatypes.KlTestKeuzelijst import KlTestKeuzelijst


class OTLAttribuutDummyTests(TestCase):
    def test_dummy_StringField(self):
        attr = OTLAttribuut(field=StringField)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertTrue(isinstance(generated_dummy_waarde, str))
        self.assertTrue(5 < len(generated_dummy_waarde) < 15)

    def test_dummy_FloatOrDecimalField(self):
        attr = OTLAttribuut(field=FloatOrDecimalField)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertTrue(isinstance(generated_dummy_waarde, float))

    def test_dummy_IntegerField(self):
        attr = OTLAttribuut(field=IntegerField)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertTrue(isinstance(generated_dummy_waarde, int))

    def test_dummy_BooleanField(self):
        attr = OTLAttribuut(field=BooleanField)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertTrue(generated_dummy_waarde in [False, True])

    def test_dummy_DateField(self):
        attr = OTLAttribuut(field=DateField)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertTrue(isinstance(generated_dummy_waarde, date))

    def test_dummy_DateTimeField(self):
        attr = OTLAttribuut(field=DateTimeField)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertTrue(isinstance(generated_dummy_waarde, datetime))

    def test_dummy_TimeField(self):
        attr = OTLAttribuut(field=TimeField)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertTrue(isinstance(generated_dummy_waarde, time))

    def test_dummy_KeuzelijstField(self):
        attr = OTLAttribuut(field=KlTestKeuzelijst)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertTrue(isinstance(generated_dummy_waarde, str))
        self.assertTrue(generated_dummy_waarde in attr.field.options.keys())

    def test_dummy_KwantWrdField(self):
        attr = OTLAttribuut(field=KwantWrdTest)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertIsNotNone(generated_dummy_waarde.waarde)
        self.assertEqual(generated_dummy_waarde.standaardEenheid, '%')

    def test_dummy_ComplexField(self):
        attr = OTLAttribuut(field=DtcTestComplexType)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertIsNotNone(generated_dummy_waarde.testStringField)
        self.assertIsNotNone(generated_dummy_waarde.testBooleanField)

    def test_dummy_UnionField(self):
        attr = OTLAttribuut(field=DtuTestUnionType)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        first = generated_dummy_waarde.unionKwantWrd.waarde is not None
        second = generated_dummy_waarde.unionString is not None
        self.assertTrue(first != second)  # either first or second is True, but not both


