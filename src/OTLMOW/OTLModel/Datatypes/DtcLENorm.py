# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KlLEKantopsluitingBijkomendeParameter import KlLEKantopsluitingBijkomendeParameter
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcLENormWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._bijkomendeParameter = OTLAttribuut(field=KlLEKantopsluitingBijkomendeParameter,
                                                 naam='bijkomendeParameter',
                                                 label='bijkomende parameter',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcLENorm.bijkomendeParameter',
                                                 definition='Het gedetailleerder typeren van de kantopsluiting.',
                                                 owner=self)

        self._norm = OTLAttribuut(field=StringField,
                                  naam='norm',
                                  label='norm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcLENorm.norm',
                                  definition='De opgelegde en beschreven standaard van de kantopsluiting.',
                                  owner=self)

    @property
    def bijkomendeParameter(self):
        """Het gedetailleerder typeren van de kantopsluiting."""
        return self._bijkomendeParameter.waarde

    @bijkomendeParameter.setter
    def bijkomendeParameter(self, value):
        self._bijkomendeParameter.set_waarde(value, owner=self._parent)

    @property
    def norm(self):
        """De opgelegde en beschreven standaard van de kantopsluiting."""
        return self._norm.waarde

    @norm.setter
    def norm(self, value):
        self._norm.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcLENorm(ComplexField, AttributeInfo):
    """Complex datatype voor de norm van het lijnvormig element."""
    naam = 'DtcLENorm'
    label = 'Norm van het lijnvormig element'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcLENorm'
    definition = 'Complex datatype voor de norm van het lijnvormig element.'
    waardeObject = DtcLENormWaarden

    def __str__(self):
        return ComplexField.__str__(self)

