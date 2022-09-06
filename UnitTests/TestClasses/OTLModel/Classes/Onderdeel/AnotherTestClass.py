# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from UnitTests.TestClasses.OTLModel.Datatypes.DtcTestComplexType import DtcTestComplexType


# Generated with OTLClassCreator. To modify: extend, do not edit
class AnotherTestClass(AIMObject):
    """Just another TestClass to test relations"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass')

        self._deprecatedString = OTLAttribuut(field=DtcTestComplexType,
                                              naam='deprecatedString',
                                              label='Deprecated Tekstveld',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass.deprecatedString',
                                              deprecated_version='2.0.0-RC3',
                                              constraints=' ',
                                              definition='Tekstveld dat niet meer gebruikt wordt',
                                              owner=self)

    @property
    def deprecatedString(self):
        """Tekstveld dat niet meer gebruikt wordt"""
        return self._deprecatedString.get_waarde()

    @deprecatedString.setter
    def deprecatedString(self, value):
        self._deprecatedString.set_waarde(value, owner=self)
