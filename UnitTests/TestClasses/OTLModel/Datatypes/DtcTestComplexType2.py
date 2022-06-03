# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from UnitTests.TestClasses.OTLModel.Datatypes.KwantWrdTest import KwantWrdTest
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTestComplexType2Waarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._testKwantWrd = OTLAttribuut(field=KwantWrdTest,
                                          naam='testKwantWrd',
                                          label='Test kwantitatieve waarde',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2.testKwantWrd',
                                          definition='Test attribuut voor Kwantitatieve waarde in een complex datatype.',
                                          owner=self)

        self._testKwantWrdMetKard = OTLAttribuut(field=KwantWrdTest,
                                                 naam='testKwantWrdMetKard',
                                                 label='Test kwantitatieve waarde met kardinaliteit',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2.testKwantWrdMetKard',
                                                 kardinaliteit_max='*',
                                                 definition='Test attribuut voor Kwantitatieve waarde met kardinaliteit > 0 in een complex datatype.',
                                                 owner=self)

        self._testStringField = OTLAttribuut(field=StringField,
                                             naam='testStringField',
                                             label='Test tekstveld',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2.testStringField',
                                             definition='Test attribuut voor tekst in een complex datatype.',
                                             owner=self)

        self._testStringFieldMetKard = OTLAttribuut(field=StringField,
                                                    naam='testStringFieldMetKard',
                                                    label='Test tekstveld met kardinaliteit',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2.testStringFieldMetKard',
                                                    kardinaliteit_max='*',
                                                    definition='Test attribuut voor tekst met kardinaliteit > 0 in een complex datatype.',
                                                    owner=self)

    @property
    def testKwantWrd(self):
        """Test attribuut voor Kwantitatieve waarde in een complex datatype."""
        return self._testKwantWrd.get_waarde()

    @testKwantWrd.setter
    def testKwantWrd(self, value):
        self._testKwantWrd.set_waarde(value, owner=self._parent)

    @property
    def testKwantWrdMetKard(self):
        """Test attribuut voor Kwantitatieve waarde met kardinaliteit > 0 in een complex datatype."""
        return self._testKwantWrdMetKard.get_waarde()

    @testKwantWrdMetKard.setter
    def testKwantWrdMetKard(self, value):
        self._testKwantWrdMetKard.set_waarde(value, owner=self._parent)

    @property
    def testStringField(self):
        """Test attribuut voor tekst in een complex datatype."""
        return self._testStringField.get_waarde()

    @testStringField.setter
    def testStringField(self, value):
        self._testStringField.set_waarde(value, owner=self._parent)

    @property
    def testStringFieldMetKard(self):
        """Test attribuut voor tekst met kardinaliteit > 0 in een complex datatype."""
        return self._testStringFieldMetKard.get_waarde()

    @testStringFieldMetKard.setter
    def testStringFieldMetKard(self, value):
        self._testStringFieldMetKard.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTestComplexType2(ComplexField, AttributeInfo):
    """Test datatype voor een complexe waarde in een complexe waarde"""
    naam = 'DtcTestComplexType2'
    label = 'Test ComplexType2'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2'
    definition = 'Test datatype voor een complexe waarde in een complexe waarde'
    waardeObject = DtcTestComplexType2Waarden

    def __str__(self):
        return ComplexField.__str__(self)

