# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.DateTimeField import DateTimeField
from UnitTests.TestClasses.OTLModel.Datatypes.DtcTestComplexType import DtcTestComplexType
from UnitTests.TestClasses.OTLModel.Datatypes.DteTestEenvoudigType import DteTestEenvoudigType
from UnitTests.TestClasses.OTLModel.Datatypes.DtuTestUnionType import DtuTestUnionType
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from UnitTests.TestClasses.OTLModel.Datatypes.KlTestKeuzelijst import KlTestKeuzelijst
from UnitTests.TestClasses.OTLModel.Datatypes.KwantWrdTest import KwantWrdTest
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.OTLModel.Datatypes.TimeField import TimeField


# Generated with OTLClassCreator. To modify: extend, do not edit
class AllCasesTestClass(AIMObject):
    """Testclass containing all possible datatypes and combinations"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._testBooleanField = OTLAttribuut(field=BooleanField,
                                              naam='testBooleanField',
                                              label='Test BooleanField',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testBooleanField',
                                              definition='Test attribuut voor BooleanField',
                                              owner=self)

        self._testComplexType = OTLAttribuut(field=DtcTestComplexType,
                                             naam='testComplexType',
                                             label='Test ComplexType',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testComplexType',
                                             definition='Test attribuut voor een complexe waarde',
                                             owner=self)

        self._testComplexTypeMetKard = OTLAttribuut(field=DtcTestComplexType,
                                                    naam='testComplexTypeMetKard',
                                                    label='Test ComplexType Met Kard',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testComplexTypeMetKard',
                                                    kardinaliteit_max='*',
                                                    definition='Test attribuut voor een complexe waarde met kardinaliteit > 1',
                                                    owner=self)

        self._testDateField = OTLAttribuut(field=DateField,
                                           naam='testDateField',
                                           label='Test DateField',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testDateField',
                                           definition='Test attribuut voor DateField',
                                           owner=self)

        self._testDateTimeField = OTLAttribuut(field=DateTimeField,
                                               naam='testDateTimeField',
                                               label='Test DateTimeField',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testDateTimeField',
                                               definition='Test attribuut voor DateTimeField',
                                               owner=self)

        self._testDecimalField = OTLAttribuut(field=FloatOrDecimalField,
                                              naam='testDecimalField',
                                              label='Test DecimalField',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testDecimalField',
                                              definition='Test attribuut voor DecimalField',
                                              owner=self)

        self._testDecimalFieldMetKard = OTLAttribuut(field=FloatOrDecimalField,
                                                     naam='testDecimalFieldMetKard',
                                                     label='Test DecimalField Met Kard',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testDecimalFieldMetKard',
                                                     kardinaliteit_max='*',
                                                     definition='Test attribuut voor DecimalField met kardinaliteit > 1',
                                                     owner=self)

        self._testEenvoudigType = OTLAttribuut(field=DteTestEenvoudigType,
                                               naam='testEenvoudigType',
                                               label='Test EenvoudigType',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testEenvoudigType',
                                               definition='Test attribuut voor een eenvoudige waarde',
                                               owner=self)

        self._testEenvoudigTypeMetKard = OTLAttribuut(field=DteTestEenvoudigType,
                                                      naam='testEenvoudigTypeMetKard',
                                                      label='Test EenvoudigType Met Kard',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testEenvoudigTypeMetKard',
                                                      kardinaliteit_max='*',
                                                      definition='Test attribuut voor een eenvoudige waarde met kardinaliteit > 1',
                                                      owner=self)

        self._testIntegerField = OTLAttribuut(field=IntegerField,
                                              naam='testIntegerField',
                                              label='Test IntegerField',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testIntegerField',
                                              definition='Test attribuut voor IntegerField',
                                              owner=self)

        self._testIntegerFieldMetKard = OTLAttribuut(field=IntegerField,
                                                     naam='testIntegerFieldMetKard',
                                                     label='Test IntegerField Met Kard',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testIntegerFieldMetKard',
                                                     kardinaliteit_max='*',
                                                     definition='Test attribuut voor IntegerField met kardinaliteit > 1',
                                                     owner=self)

        self._testKeuzelijst = OTLAttribuut(field=KlTestKeuzelijst,
                                            naam='testKeuzelijst',
                                            label='Test Keuzelijst',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKeuzelijst',
                                            definition='Test attribuut voor een keuzelijst',
                                            owner=self)

        self._testKeuzelijstMetKard = OTLAttribuut(field=KlTestKeuzelijst,
                                                   naam='testKeuzelijstMetKard',
                                                   label='Test Keuzelijst Met Kard',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKeuzelijstMetKard',
                                                   kardinaliteit_max='*',
                                                   definition='Test attribuut voor een keuzelijst met kardinaliteit > 1',
                                                   owner=self)

        self._testKwantWrd = OTLAttribuut(field=KwantWrdTest,
                                          naam='testKwantWrd',
                                          label='Test KwantWrd',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKwantWrd',
                                          definition='Test attribuut voor een kwantitatieve waarde',
                                          owner=self)

        self._testKwantWrdMetKard = OTLAttribuut(field=KwantWrdTest,
                                                 naam='testKwantWrdMetKard',
                                                 label='Test KwantWrd Met Kard',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKwantWrdMetKard',
                                                 kardinaliteit_max='*',
                                                 definition='Test attribuut voor een kwantitatieve waarde met kardinaliteit > 1',
                                                 owner=self)

        self._testStringField = OTLAttribuut(field=StringField,
                                             naam='testStringField',
                                             label='Test StringField',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testStringField',
                                             definition='Test attribuut voor StringField',
                                             owner=self)

        self._testStringFieldMetKard = OTLAttribuut(field=StringField,
                                                    naam='testStringFieldMetKard',
                                                    label='Test StringField Met Kard',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testStringFieldMetKard',
                                                    kardinaliteit_max='*',
                                                    definition='Test attribuut voor StringField met kardinaliteit > 1',
                                                    owner=self)

        self._testTimeField = OTLAttribuut(field=TimeField,
                                           naam='testTimeField',
                                           label='Test TimeField',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testTimeField',
                                           definition='Test attribuut voor TimeField',
                                           owner=self)

        self._testUnionType = OTLAttribuut(field=DtuTestUnionType,
                                           naam='testUnionType',
                                           label='Test UnionType',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testUnionType',
                                           definition='Test attribuut voor een union type',
                                           owner=self)

        self._testUnionTypeMetKard = OTLAttribuut(field=DtuTestUnionType,
                                                  naam='testUnionTypeMetKard',
                                                  label='Test UnionTypeMetKard',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testUnionTypeMetKard',
                                                  kardinaliteit_max='*',
                                                  definition='Test attribuut voor een union type met kardinaliteit > 1',
                                                  owner=self)

    @property
    def testBooleanField(self):
        """Test attribuut voor BooleanField"""
        return self._testBooleanField.get_waarde()

    @testBooleanField.setter
    def testBooleanField(self, value):
        self._testBooleanField.set_waarde(value, owner=self)

    @property
    def testComplexType(self):
        """Test attribuut voor een complexe waarde"""
        return self._testComplexType.get_waarde()

    @testComplexType.setter
    def testComplexType(self, value):
        self._testComplexType.set_waarde(value, owner=self)

    @property
    def testComplexTypeMetKard(self):
        """Test attribuut voor een complexe waarde met kardinaliteit > 1"""
        return self._testComplexTypeMetKard.get_waarde()

    @testComplexTypeMetKard.setter
    def testComplexTypeMetKard(self, value):
        self._testComplexTypeMetKard.set_waarde(value, owner=self)

    @property
    def testDateField(self):
        """Test attribuut voor DateField"""
        return self._testDateField.get_waarde()

    @testDateField.setter
    def testDateField(self, value):
        self._testDateField.set_waarde(value, owner=self)

    @property
    def testDateTimeField(self):
        """Test attribuut voor DateTimeField"""
        return self._testDateTimeField.get_waarde()

    @testDateTimeField.setter
    def testDateTimeField(self, value):
        self._testDateTimeField.set_waarde(value, owner=self)

    @property
    def testDecimalField(self):
        """Test attribuut voor DecimalField"""
        return self._testDecimalField.get_waarde()

    @testDecimalField.setter
    def testDecimalField(self, value):
        self._testDecimalField.set_waarde(value, owner=self)

    @property
    def testDecimalFieldMetKard(self):
        """Test attribuut voor DecimalField met kardinaliteit > 1"""
        return self._testDecimalFieldMetKard.get_waarde()

    @testDecimalFieldMetKard.setter
    def testDecimalFieldMetKard(self, value):
        self._testDecimalFieldMetKard.set_waarde(value, owner=self)

    @property
    def testEenvoudigType(self):
        """Test attribuut voor een eenvoudige waarde"""
        return self._testEenvoudigType.get_waarde()

    @testEenvoudigType.setter
    def testEenvoudigType(self, value):
        self._testEenvoudigType.set_waarde(value, owner=self)

    @property
    def testEenvoudigTypeMetKard(self):
        """Test attribuut voor een eenvoudige waarde met kardinaliteit > 1"""
        return self._testEenvoudigTypeMetKard.get_waarde()

    @testEenvoudigTypeMetKard.setter
    def testEenvoudigTypeMetKard(self, value):
        self._testEenvoudigTypeMetKard.set_waarde(value, owner=self)

    @property
    def testIntegerField(self):
        """Test attribuut voor IntegerField"""
        return self._testIntegerField.get_waarde()

    @testIntegerField.setter
    def testIntegerField(self, value):
        self._testIntegerField.set_waarde(value, owner=self)

    @property
    def testIntegerFieldMetKard(self):
        """Test attribuut voor IntegerField met kardinaliteit > 1"""
        return self._testIntegerFieldMetKard.get_waarde()

    @testIntegerFieldMetKard.setter
    def testIntegerFieldMetKard(self, value):
        self._testIntegerFieldMetKard.set_waarde(value, owner=self)

    @property
    def testKeuzelijst(self):
        """Test attribuut voor een keuzelijst"""
        return self._testKeuzelijst.get_waarde()

    @testKeuzelijst.setter
    def testKeuzelijst(self, value):
        self._testKeuzelijst.set_waarde(value, owner=self)

    @property
    def testKeuzelijstMetKard(self):
        """Test attribuut voor een keuzelijst met kardinaliteit > 1"""
        return self._testKeuzelijstMetKard.get_waarde()

    @testKeuzelijstMetKard.setter
    def testKeuzelijstMetKard(self, value):
        self._testKeuzelijstMetKard.set_waarde(value, owner=self)

    @property
    def testKwantWrd(self):
        """Test attribuut voor een kwantitatieve waarde"""
        return self._testKwantWrd.get_waarde()

    @testKwantWrd.setter
    def testKwantWrd(self, value):
        self._testKwantWrd.set_waarde(value, owner=self)

    @property
    def testKwantWrdMetKard(self):
        """Test attribuut voor een kwantitatieve waarde met kardinaliteit > 1"""
        return self._testKwantWrdMetKard.get_waarde()

    @testKwantWrdMetKard.setter
    def testKwantWrdMetKard(self, value):
        self._testKwantWrdMetKard.set_waarde(value, owner=self)

    @property
    def testStringField(self):
        """Test attribuut voor StringField"""
        return self._testStringField.get_waarde()

    @testStringField.setter
    def testStringField(self, value):
        self._testStringField.set_waarde(value, owner=self)

    @property
    def testStringFieldMetKard(self):
        """Test attribuut voor StringField met kardinaliteit > 1"""
        return self._testStringFieldMetKard.get_waarde()

    @testStringFieldMetKard.setter
    def testStringFieldMetKard(self, value):
        self._testStringFieldMetKard.set_waarde(value, owner=self)

    @property
    def testTimeField(self):
        """Test attribuut voor TimeField"""
        return self._testTimeField.get_waarde()

    @testTimeField.setter
    def testTimeField(self, value):
        self._testTimeField.set_waarde(value, owner=self)

    @property
    def testUnionType(self):
        """Test attribuut voor een union type"""
        return self._testUnionType.get_waarde()

    @testUnionType.setter
    def testUnionType(self, value):
        self._testUnionType.set_waarde(value, owner=self)

    @property
    def testUnionTypeMetKard(self):
        """Test attribuut voor een union type met kardinaliteit > 1"""
        return self._testUnionTypeMetKard.get_waarde()

    @testUnionTypeMetKard.setter
    def testUnionTypeMetKard(self, value):
        self._testUnionTypeMetKard.set_waarde(value, owner=self)
