# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class DteTestEenvoudigTypeWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._waarde = OTLAttribuut(field=StringField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType.waarde',
                                    definition='De string die het eenvoudige test datatype voorstelt.',
                                    owner=self)

    @property
    def waarde(self):
        """De string die het eenvoudige test datatype voorstelt."""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class DteTestEenvoudigType(OTLField, AttributeInfo):
    """Beschrijft een tekst van een eenvoudig type."""
    naam = 'DteTestEenvoudigType'
    label = 'Test EenvoudigType'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType'
    definition = 'Beschrijft een tekst van een eenvoudig type.'
    waarde_shortcut_applicable = True
    waardeObject = DteTestEenvoudigTypeWaarden

    def __str__(self):
        return OTLField.__str__(self)

