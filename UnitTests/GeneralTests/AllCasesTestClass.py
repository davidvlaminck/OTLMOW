# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObject
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.KlAansluitstukMateriaal import KlAansluitstukMateriaal
from OTLMOW.OTLModel.Datatypes.StringField import StringField



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


class AllCasesTestClass(OTLObject):
    """Test klasse die alle mogelijke cases en combinaties bevat"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        OTLObject.__init__(self)

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

        self._materiaal = OTLAttribuut(field=KlAansluitstukMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitmof.materiaal',
                                       definition='Het materiaal van de aansluitmof.',
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

    @property
    def materiaal(self):
        """Het materiaal van de aansluitmof."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
