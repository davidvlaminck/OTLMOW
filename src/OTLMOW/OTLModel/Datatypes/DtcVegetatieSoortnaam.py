# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVegetatieSoortnaamWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._code = OTLAttribuut(field=StringField,
                                  naam='code',
                                  label='code',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVegetatieSoortnaam.code',
                                  usagenote='De GBIF code is een unieke gestandaardiseerde code uitgegeven door het GBIF (the Global Biodiversity Information Facility - GBIF.org)',
                                  definition='De unieke identificator voor de soort van het vegetatie-element.',
                                  owner=self)

        self._soortnaamNederlands = OTLAttribuut(field=StringField,
                                                 naam='soortnaamNederlands',
                                                 label='soortnaam nederlands',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVegetatieSoortnaam.soortnaamNederlands',
                                                 definition='De Nederlandse soortnaam van de beplanting.',
                                                 owner=self)

        self._soortnaamWetenschappelijk = OTLAttribuut(field=StringField,
                                                       naam='soortnaamWetenschappelijk',
                                                       label='soortnaam wetenschappelijk',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVegetatieSoortnaam.soortnaamWetenschappelijk',
                                                       definition='De wetenschappelijke soortnaam van de beplanting.',
                                                       owner=self)

    @property
    def code(self):
        """De unieke identificator voor de soort van het vegetatie-element."""
        return self._code.get_waarde()

    @code.setter
    def code(self, value):
        self._code.set_waarde(value, owner=self._parent)

    @property
    def soortnaamNederlands(self):
        """De Nederlandse soortnaam van de beplanting."""
        return self._soortnaamNederlands.get_waarde()

    @soortnaamNederlands.setter
    def soortnaamNederlands(self, value):
        self._soortnaamNederlands.set_waarde(value, owner=self._parent)

    @property
    def soortnaamWetenschappelijk(self):
        """De wetenschappelijke soortnaam van de beplanting."""
        return self._soortnaamWetenschappelijk.get_waarde()

    @soortnaamWetenschappelijk.setter
    def soortnaamWetenschappelijk(self, value):
        self._soortnaamWetenschappelijk.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVegetatieSoortnaam(ComplexField, AttributeInfo):
    """Complex datatype voor de soortnaam en code van een begroeiing."""
    naam = 'DtcVegetatieSoortnaam'
    label = 'Vegetatie soortnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVegetatieSoortnaam'
    definition = 'Complex datatype voor de soortnaam en code van een begroeiing.'
    waardeObject = DtcVegetatieSoortnaamWaarden

    def __str__(self):
        return ComplexField.__str__(self)

