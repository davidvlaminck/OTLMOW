# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


class DtcTestComplexType2Waarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)

        self._testStringField = OTLAttribuut(field=StringField,
                                             naam='testStringField',
                                             label='testStringField',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTestComplexTypeWaarden.testStringField',
                                             definition='Test attribuut voor StringField',
                                             owner=self)

        self._testStringFieldMetKard = OTLAttribuut(field=StringField,
                                                    naam='testStringFieldMetKard',
                                                    label='testStringFieldMetKard',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTestComplexTypeWaarden.testStringFieldMetKard',
                                                    definition='Test attribuut voor StringField met kardinaliteit > 1',
                                                    kardinaliteit_max='*',
                                                    owner=self)

        self._testKwantWrd = OTLAttribuut(field=KwantWrdTest,
                                          naam='testKwantWrd',
                                          label='testKwantWrd',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTestComplexTypeWaarden.testKwantWrd',
                                          definition='Test attribuut voor Kwantitatieve waarde',
                                          owner=self)

        self._testKwantWrdMetKard = OTLAttribuut(field=KwantWrdTest,
                                                 naam='testKwantWrdMetKard',
                                                 label='testKwantWrdMetKard',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTestComplexTypeWaarden.testKwantWrdMetKard',
                                                 definition='Test attribuut voor Kwantitatieve waarde met kardinaliteit > 1',
                                                 kardinaliteit_max='*',
                                                 owner=self)

    @property
    def testStringFieldMetKard(self):
        """Test attribuut voor StringField met kardinaliteit > 1"""
        return self._testStringFieldMetKard.waarde

    @testStringFieldMetKard.setter
    def testStringFieldMetKard(self, value):
        self._testStringFieldMetKard.set_waarde(value, owner=self)

    @property
    def testStringField(self):
        """Test attribuut voor StringField"""
        return self._testStringField.waarde

    @testStringField.setter
    def testStringField(self, value):
        self._testStringField.set_waarde(value, owner=self)

    @property
    def testKwantWrdMetKard(self):
        """Test attribuut voor Kwantitatieve waarde met kardinaliteit > 1"""
        return self._testKwantWrdMetKard.waarde

    @testKwantWrdMetKard.setter
    def testKwantWrdMetKard(self, value):
        self._testKwantWrdMetKard.set_waarde(value, owner=self)

    @property
    def testKwantWrd(self):
        """Test attribuut voor Kwantitatieve waarde"""
        return self._testKwantWrd.waarde

    @testKwantWrd.setter
    def testKwantWrd(self, value):
        self._testKwantWrd.set_waarde(value, owner=self)


class DtcTestComplexType2(ComplexField, AttributeInfo):
    """Complex datatype 2 voor test doeleinden"""
    naam = 'DtcTestComplexType2'
    label = 'Test complex type 2'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTestComplexType2'
    definition = 'Complex datatype 2 voor test doeleinden'
    waardeObject = DtcTestComplexType2Waarden

    def __str__(self):
        return ComplexField.__str__(self)


class DtcTestComplexTypeWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)

        self._testBooleanField = OTLAttribuut(field=BooleanField,
                                              naam='testBooleanField',
                                              label='testBooleanField',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTestComplexTypeWaarden.testBooleanField',
                                              definition='Test attribuut voor BooleanField',
                                              owner=self)

        self._testStringField = OTLAttribuut(field=StringField,
                                             naam='testStringField',
                                             label='testStringField',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTestComplexTypeWaarden.testStringField',
                                             definition='Test attribuut voor StringField',
                                             owner=self)

        self._testStringFieldMetKard = OTLAttribuut(field=StringField,
                                                    naam='testStringFieldMetKard',
                                                    label='testStringFieldMetKard',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTestComplexTypeWaarden.testStringFieldMetKard',
                                                    definition='Test attribuut voor StringField met kardinaliteit > 1',
                                                    kardinaliteit_max='*',
                                                    owner=self)

        self._testKwantWrd = OTLAttribuut(field=KwantWrdTest,
                                          naam='testKwantWrd',
                                          label='testKwantWrd',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTestComplexTypeWaarden.testKwantWrd',
                                          definition='Test attribuut voor Kwantitatieve waarde',
                                          owner=self)

        self._testKwantWrdMetKard = OTLAttribuut(field=KwantWrdTest,
                                                 naam='testKwantWrdMetKard',
                                                 label='testKwantWrdMetKard',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTestComplexTypeWaarden.testKwantWrdMetKard',
                                                 definition='Test attribuut voor Kwantitatieve waarde met kardinaliteit > 1',
                                                 kardinaliteit_max='*',
                                                 owner=self)

        self._testComplexType2 = OTLAttribuut(field=DtcTestComplexType2,
                                              naam='testComplexType2',
                                              label='testComplexType2',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testComplexType2',
                                              definition='Test attribuut 2 voor een complexe waarde',
                                              owner=self)

        self._testComplexType2MetKard = OTLAttribuut(field=DtcTestComplexType2,
                                                     naam='testComplexTypeMetKard2',
                                                     label='testComplexTypeMetKard2',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testComplexType2MetKard',
                                                     definition='Test attribuut 2 voor een complexe waarde met kardinaliteit > 1',
                                                     kardinaliteit_max='*',
                                                     owner=self)

    @property
    def testComplexType2MetKard(self):
        """Test attribuut 2 voor een complexe waarde met kardinaliteit > 1"""
        return self._testComplexType2MetKard.waarde

    @testComplexType2MetKard.setter
    def testComplexType2MetKard(self, value):
        self._testComplexType2MetKard.set_waarde(value, owner=self)

    @property
    def testComplexType2(self):
        """Test attribuut 2 voor een complexe waarde"""
        return self._testComplexType2.waarde

    @testComplexType2.setter
    def testComplexType2(self, value):
        self._testComplexType2.set_waarde(value, owner=self)

    @property
    def testStringFieldMetKard(self):
        """Test attribuut voor StringField met kardinaliteit > 1"""
        return self._testStringFieldMetKard.waarde

    @testStringFieldMetKard.setter
    def testStringFieldMetKard(self, value):
        self._testStringFieldMetKard.set_waarde(value, owner=self)

    @property
    def testStringField(self):
        """Test attribuut voor StringField"""
        return self._testStringField.waarde

    @testStringField.setter
    def testStringField(self, value):
        self._testStringField.set_waarde(value, owner=self)

    @property
    def testBooleanField(self):
        """Test attribuut voor BooleanField"""
        return self._testBooleanField.waarde

    @testBooleanField.setter
    def testBooleanField(self, value):
        self._testBooleanField.set_waarde(value, owner=self)

    @property
    def testKwantWrdMetKard(self):
        """Test attribuut voor Kwantitatieve waarde met kardinaliteit > 1"""
        return self._testKwantWrdMetKard.waarde

    @testKwantWrdMetKard.setter
    def testKwantWrdMetKard(self, value):
        self._testKwantWrdMetKard.set_waarde(value, owner=self)

    @property
    def testKwantWrd(self):
        """Test attribuut voor Kwantitatieve waarde"""
        return self._testKwantWrd.waarde

    @testKwantWrd.setter
    def testKwantWrd(self, value):
        self._testKwantWrd.set_waarde(value, owner=self)


class DtcTestComplexType(ComplexField, AttributeInfo):
    """Complex datatype voor test doeleinden"""
    naam = 'DtcTestComplexType'
    label = 'Test complex type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTestComplexType'
    definition = 'Complex datatype voor test doeleinden'
    waardeObject = DtcTestComplexTypeWaarden

    def __str__(self):
        return ComplexField.__str__(self)


class KwantWrdTestWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest.standaardEenheid',
                                              usagenote='"V"^^cdt:ucumunit',
                                              constraints='"V"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt.',
                                              owner=self)

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.',
                                    owner=self)

    @property
    def standaardEenheid(self):
        """De standaard eenheid bij dit datatype is uitgedrukt."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self):
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.waarde

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdTest(OTLField, AttributeInfo):
    """Een kwantitatieve waarde die een test voorstelt."""
    naam = 'KwantWrdTest'
    label = 'Kwantitatieve waarde test'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest'
    definition = 'Een kwantitatieve waarde die een test voorstelt.'
    waardeObject = KwantWrdTestWaarden

    def __str__(self):
        return OTLField.__str__(self)


class AllCasesTestClass(AIMObject):
    """Test klasse die alle mogelijke cases en combinaties bevat"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)

        self._testDecimalNumberField = OTLAttribuut(field=FloatOrDecimalField,
                                                    naam='testFloatOrDecimalField',
                                                    label='testFloatOrDecimalField',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testFloatOrDecimalField',
                                                    definition='Test attribuut voor FloatOrDecimalField',
                                                    owner=self)

        self._testDecimalNumberFieldMetKard = OTLAttribuut(field=FloatOrDecimalField,
                                                           naam='testFloatOrDecimalFieldMetKard',
                                                           label='testFloatOrDecimalFielddMetKard',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testFloatOrDecimalFieldMetKard',
                                                           definition='Test attribuut voor FloatOrDecimalField met kardinaliteit > 1',
                                                           kardinaliteit_max='*',
                                                           owner=self)

        self._testBooleanField = OTLAttribuut(field=BooleanField,
                                              naam='testBooleanField',
                                              label='testBooleanField',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testBooleanField',
                                              definition='Test attribuut voor BooleanField',
                                              owner=self)

        self._testStringField = OTLAttribuut(field=StringField,
                                             naam='testStringField',
                                             label='testStringField',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testStringField',
                                             definition='Test attribuut voor StringField',
                                             owner=self)

        self._testStringFieldMetKard = OTLAttribuut(field=StringField,
                                                    naam='testStringFieldMetKard',
                                                    label='testStringFieldMetKard',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testStringFieldMetKard',
                                                    definition='Test attribuut voor StringField met kardinaliteit > 1',
                                                    kardinaliteit_max='*',
                                                    owner=self)

        self._testKwantWrd = OTLAttribuut(field=KwantWrdTest,
                                          naam='testKwantWrd',
                                          label='testKwantWrd',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKwantWrd',
                                          definition='Test attribuut voor Kwantitatieve waarde',
                                          owner=self)

        self._testKwantWrdMetKard = OTLAttribuut(field=KwantWrdTest,
                                                 naam='testKwantWrdMetKard',
                                                 label='testKwantWrdMetKard',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKwantWrdMetKard',
                                                 definition='Test attribuut voor Kwantitatieve waarde met kardinaliteit > 1',
                                                 kardinaliteit_max='*',
                                                 owner=self)

        self._testComplexType = OTLAttribuut(field=DtcTestComplexType,
                                             naam='testComplexType',
                                             label='testComplexType',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testComplexType',
                                             definition='Test attribuut voor een complexe waarde',
                                             owner=self)

        self._testComplexTypeMetKard = OTLAttribuut(field=DtcTestComplexType,
                                                    naam='testComplexTypeMetKard',
                                                    label='testComplexTypeMetKard',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testComplexTypeMetKard',
                                                    definition='Test attribuut voor een complexe waarde met kardinaliteit > 1',
                                                    kardinaliteit_max='*',
                                                    owner=self)

    @property
    def testComplexTypeMetKard(self):
        """Test attribuut voor een complexe waarde met kardinaliteit > 1"""
        return self._testComplexTypeMetKard.waarde

    @testComplexTypeMetKard.setter
    def testComplexTypeMetKard(self, value):
        self._testComplexTypeMetKard.set_waarde(value, owner=self)

    @property
    def testComplexType(self):
        """Test attribuut voor een complexe waarde"""
        return self._testComplexType.waarde

    @testComplexType.setter
    def testComplexType(self, value):
        self._testComplexType.set_waarde(value, owner=self)

    @property
    def testDecimalNumberFieldMetKard(self):
        """Test attribuut voor DecimalNumberField met kardinaliteit > 1"""
        return self._testDecimalNumberFieldMetKard.waarde

    @testDecimalNumberFieldMetKard.setter
    def testDecimalNumberFieldMetKard(self, value):
        self._testDecimalNumberFieldMetKard.set_waarde(value, owner=self)

    @property
    def testDecimalNumberField(self):
        """Test attribuut voor DecimalNumberField"""
        return self._testDecimalNumberField.waarde

    @testDecimalNumberField.setter
    def testDecimalNumberField(self, value):
        self._testDecimalNumberField.set_waarde(value, owner=self)

    @property
    def testBooleanField(self):
        """Test attribuut voor BooleanField"""
        return self._testBooleanField.waarde

    @testBooleanField.setter
    def testBooleanField(self, value):
        self._testBooleanField.set_waarde(value, owner=self)

    @property
    def testStringFieldMetKard(self):
        """Test attribuut voor StringField met kardinaliteit > 1"""
        return self._testStringFieldMetKard.waarde

    @testStringFieldMetKard.setter
    def testStringFieldMetKard(self, value):
        self._testStringFieldMetKard.set_waarde(value, owner=self)

    @property
    def testStringField(self):
        """Test attribuut voor StringField"""
        return self._testStringField.waarde

    @testStringField.setter
    def testStringField(self, value):
        self._testStringField.set_waarde(value, owner=self)

    @property
    def testKwantWrdMetKard(self):
        """Test attribuut voor Kwantitatieve waarde met kardinaliteit > 1"""
        return self._testKwantWrdMetKard.waarde

    @testKwantWrdMetKard.setter
    def testKwantWrdMetKard(self, value):
        self._testKwantWrdMetKard.set_waarde(value, owner=self)

    @property
    def testKwantWrd(self):
        """Test attribuut voor Kwantitatieve waarde"""
        return self._testKwantWrd.waarde

    @testKwantWrd.setter
    def testKwantWrd(self, value):
        self._testKwantWrd.set_waarde(value, owner=self)
