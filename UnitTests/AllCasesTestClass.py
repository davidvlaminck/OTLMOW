# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLMOW.OTLModel.Datatypes.UnionWaarden import UnionWaarden


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
        return self._testStringFieldMetKard.get_waarde()

    @testStringFieldMetKard.setter
    def testStringFieldMetKard(self, value):
        self._testStringFieldMetKard.set_waarde(value, owner=self)

    @property
    def testStringField(self):
        """Test attribuut voor StringField"""
        return self._testStringField.get_waarde()

    @testStringField.setter
    def testStringField(self, value):
        self._testStringField.set_waarde(value, owner=self)

    @property
    def testKwantWrdMetKard(self):
        """Test attribuut voor Kwantitatieve waarde met kardinaliteit > 1"""
        return self._testKwantWrdMetKard.get_waarde()

    @testKwantWrdMetKard.setter
    def testKwantWrdMetKard(self, value):
        self._testKwantWrdMetKard.set_waarde(value, owner=self)

    @property
    def testKwantWrd(self):
        """Test attribuut voor Kwantitatieve waarde"""
        return self._testKwantWrd.get_waarde()

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
        return self._testComplexType2MetKard.get_waarde()

    @testComplexType2MetKard.setter
    def testComplexType2MetKard(self, value):
        self._testComplexType2MetKard.set_waarde(value, owner=self)

    @property
    def testComplexType2(self):
        """Test attribuut 2 voor een complexe waarde"""
        return self._testComplexType2.get_waarde()

    @testComplexType2.setter
    def testComplexType2(self, value):
        self._testComplexType2.set_waarde(value, owner=self)

    @property
    def testStringFieldMetKard(self):
        """Test attribuut voor StringField met kardinaliteit > 1"""
        return self._testStringFieldMetKard.get_waarde()

    @testStringFieldMetKard.setter
    def testStringFieldMetKard(self, value):
        self._testStringFieldMetKard.set_waarde(value, owner=self)

    @property
    def testStringField(self):
        """Test attribuut voor StringField"""
        return self._testStringField.get_waarde()

    @testStringField.setter
    def testStringField(self, value):
        self._testStringField.set_waarde(value, owner=self)

    @property
    def testBooleanField(self):
        """Test attribuut voor BooleanField"""
        return self._testBooleanField.get_waarde()

    @testBooleanField.setter
    def testBooleanField(self, value):
        self._testBooleanField.set_waarde(value, owner=self)

    @property
    def testKwantWrdMetKard(self):
        """Test attribuut voor Kwantitatieve waarde met kardinaliteit > 1"""
        return self._testKwantWrdMetKard.get_waarde()

    @testKwantWrdMetKard.setter
    def testKwantWrdMetKard(self, value):
        self._testKwantWrdMetKard.set_waarde(value, owner=self)

    @property
    def testKwantWrd(self):
        """Test attribuut voor Kwantitatieve waarde"""
        return self._testKwantWrd.get_waarde()

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


class DteTestEenvoudigTypeWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._waarde = OTLAttribuut(field=StringField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType.waarde',
                                    usagenote='Alle karakters zijn toegelaten',
                                    definition='Beschrijft een tekst van een eenvoudig type.',
                                    owner=self)

    @property
    def waarde(self):
        """Beschrijft een tekst van een eenvoudig type."""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


class DteTestEenvoudigType(OTLField, AttributeInfo):
    """Beschrijft een attribuut voor een eenvoudig type"""
    naam = 'DteTestEenvoudigType'
    label = 'Test Eenvoudig Type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType'
    definition = 'Beschrijft een attribuut voor een eenvoudig type'
    waardeObject = DteTestEenvoudigTypeWaarden

    def __str__(self):
        return OTLField.__str__(self)


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
        return self._waarde.get_waarde()

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


class DtuTestUnionTypeWaarden(AttributeInfo, UnionWaarden):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        UnionWaarden.__init__(self)
        self._unionKwantWrd = OTLAttribuut(field=KwantWrdTest,
                                           naam='UnionKwantWrd',
                                           label='Union Kwant Wrd',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuTestUnionType.unionKwantWrd',
                                           kardinaliteit_min='0',
                                           definition='De kwantitatieve waarde van deze union type.',
                                           owner=self)

        self._unionString = OTLAttribuut(field=StringField,
                                         naam='unionString',
                                         label='Union String',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuTestUnionType.unionString',
                                         kardinaliteit_min='0',
                                         definition='De tekstuele waarde van deze union type',
                                         owner=self)

    @property
    def unionKwantWrd(self):
        """De kwantitatieve waarde van deze union type."""
        return self._unionKwantWrd.get_waarde()

    @unionKwantWrd.setter
    def unionKwantWrd(self, value):
        self._unionKwantWrd.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_unionKwantWrd')

    @property
    def unionString(self):
        """De tekstuele waarde van deze union type"""
        return self._unionString.get_waarde()

    @unionString.setter
    def unionString(self, value):
        self._unionString.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_unionString')


class DtuTestUnionType(UnionTypeField, AttributeInfo):
    """Test Union datatype"""
    naam = 'DtuTestUnionType'
    label = 'TestUnionType'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuTestUnionType'
    definition = 'Union datatype om testen mee uit te voeren.'
    waardeObject = DtuTestUnionTypeWaarden

    def __str__(self):
        return UnionTypeField.__str__(self)


class KlTestKeuzelijst(KeuzelijstField):
    """Keuzelijst met test waarden."""
    naam = 'KlTestKeuzelijst'
    label = 'Test Keuzelijst'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlTestKeuzelijst'
    definition = 'Keuzelijst met test waarden.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAIMToestand'
    options = {
        'waarde 1': KeuzelijstWaarde(invulwaarde='waarde-1',
                                     label='waarde 1',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/waarde-1'),
        'waarde 2': KeuzelijstWaarde(invulwaarde='waarde-2',
                                     label='waarde 2',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/waarde-2'),
        'waarde 3': KeuzelijstWaarde(invulwaarde='waarde-3',
                                     label='waarde 3',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/waarde-3')
    }


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

        self._testUnionType = OTLAttribuut(field=DtuTestUnionType,
                                           naam='testUnionType',
                                           label='testUnionType',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testUnionType',
                                           definition='Test attribuut voor testUnionType.',
                                           owner=self)

        self._testUnionTypeMetKard = OTLAttribuut(field=DtuTestUnionType,
                                                  naam='testUnionTypeMetKard',
                                                  label='testUnionTypeMetKard',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testUnionTypeMetKard',
                                                  definition='Test attribuut voor testUnionType met kardinaliteit > 1.',
                                                  kardinaliteit_max='*',
                                                  owner=self)

        self._testEenvoudigType = OTLAttribuut(field=DteTestEenvoudigType,
                                               naam='TestEenvoudigType',
                                               label='Test Eenvoudig Type',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.DteTestEenvoudigType',
                                               definition='Test attribuut voor TestEenvoudigType.')

        self._testKeuzelijst = OTLAttribuut(field=KlTestKeuzelijst,
                                            naam='testKeuzelijst',
                                            label='test Keuzelijst',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AllCasesTestClass.KltestKeuzelijst',
                                            definition='Test attribuut voor TestKeuzelijst',
                                            owner=self)

        self._testKeuzelijstMetKard = OTLAttribuut(field=KlTestKeuzelijst,
                                                   naam='testKeuzelijstMetKard',
                                                   label='test KeuzelijstMetKard',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AllCasesTestClass.KltestKeuzelijst',
                                                   definition='Test attribuut voor TestKeuzelijstMetKard',
                                                   kardinaliteit_max='*',
                                                   owner=self)

    @property
    def testComplexTypeMetKard(self):
        """Test attribuut voor een complexe waarde met kardinaliteit > 1"""
        return self._testComplexTypeMetKard.get_waarde()

    @testComplexTypeMetKard.setter
    def testComplexTypeMetKard(self, value):
        self._testComplexTypeMetKard.set_waarde(value, owner=self)

    @property
    def testComplexType(self):
        """Test attribuut voor een complexe waarde"""
        return self._testComplexType.get_waarde()

    @testComplexType.setter
    def testComplexType(self, value):
        self._testComplexType.set_waarde(value, owner=self)

    @property
    def testDecimalNumberFieldMetKard(self):
        """Test attribuut voor DecimalNumberField met kardinaliteit > 1"""
        return self._testDecimalNumberFieldMetKard.get_waarde()

    @testDecimalNumberFieldMetKard.setter
    def testDecimalNumberFieldMetKard(self, value):
        self._testDecimalNumberFieldMetKard.set_waarde(value, owner=self)

    @property
    def testDecimalNumberField(self):
        """Test attribuut voor DecimalNumberField"""
        return self._testDecimalNumberField.get_waarde()

    @testDecimalNumberField.setter
    def testDecimalNumberField(self, value):
        self._testDecimalNumberField.set_waarde(value, owner=self)

    @property
    def testBooleanField(self):
        """Test attribuut voor BooleanField"""
        return self._testBooleanField.get_waarde()

    @testBooleanField.setter
    def testBooleanField(self, value):
        self._testBooleanField.set_waarde(value, owner=self)

    @property
    def testStringFieldMetKard(self):
        """Test attribuut voor StringField met kardinaliteit > 1"""
        return self._testStringFieldMetKard.get_waarde()

    @testStringFieldMetKard.setter
    def testStringFieldMetKard(self, value):
        self._testStringFieldMetKard.set_waarde(value, owner=self)

    @property
    def testStringField(self):
        """Test attribuut voor StringField"""
        return self._testStringField.get_waarde()

    @testStringField.setter
    def testStringField(self, value):
        self._testStringField.set_waarde(value, owner=self)

    @property
    def testKwantWrdMetKard(self):
        """Test attribuut voor Kwantitatieve waarde met kardinaliteit > 1"""
        return self._testKwantWrdMetKard.get_waarde()

    @testKwantWrdMetKard.setter
    def testKwantWrdMetKard(self, value):
        self._testKwantWrdMetKard.set_waarde(value, owner=self)

    @property
    def testKwantWrd(self):
        """Test attribuut voor Kwantitatieve waarde"""
        return self._testKwantWrd.get_waarde()

    @testKwantWrd.setter
    def testKwantWrd(self, value):
        self._testKwantWrd.set_waarde(value, owner=self)

    @property
    def testUnionType(self):
        """Test attribuut voor testUnionType."""
        return self._testUnionType.get_waarde()

    @testUnionType.setter
    def testUnionType(self, value):
        self._testUnionType.set_waarde(value, owner=self)

    @property
    def testUnionTypeMetKard(self):
        """Test attribuut voor testUnionType met kardinaliteit > 1."""
        return self._testUnionTypeMetKard.get_waarde()

    @testUnionTypeMetKard.setter
    def testUnionTypeMetKard(self, value):
        self._testUnionTypeMetKard.set_waarde(value, owner=self)

    @property
    def testEenvoudigType(self):
        """Test attribuut voor TestEenvoudigType."""
        return self._testEenvoudigType.get_waarde()

    @testEenvoudigType.setter
    def testEenvoudigType(self, value):
        self._testEenvoudigType.set_waarde(value, owner=self)

    @property
    def testKeuzelijst(self):
        """Test attribuut voor TestKeuzelijst."""
        return self._testKeuzelijst.get_waarde()

    @testKeuzelijst.setter
    def testKeuzelijst(self, value):
        self._testKeuzelijst.set_waarde(value, owner=self)

    @property
    def testKeuzelijstMetKard(self):
        """Test attribuut voor TestKeuzelijst met kardinaliteit > 1."""
        return self._testKeuzelijstMetKard.get_waarde()

    @testKeuzelijstMetKard.setter
    def testKeuzelijstMetKard(self, value):
        self._testKeuzelijstMetKard.set_waarde(value, owner=self)
