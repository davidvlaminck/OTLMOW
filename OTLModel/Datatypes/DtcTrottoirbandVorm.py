# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KlLETrottoirbandVorm import KlLETrottoirbandVorm
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTrottoirbandVormWaarden(AttributeInfo):
    def __init__(self):
        self._breedte = OTLAttribuut(field=KwantWrdInCentimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTrottoirbandVorm.breedte',
                                     definition='De breedte van de trottoirband.')

        self._dikte = OTLAttribuut(field=KwantWrdInCentimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTrottoirbandVorm.dikte',
                                   definition='De dikte van de trottoirband.')

        self._vorm = OTLAttribuut(field=KlLETrottoirbandVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTrottoirbandVorm.vorm',
                                  definition='De vorm van de trottoirband.')

    @property
    def breedte(self):
        """De breedte van de trottoirband."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value)

    @property
    def dikte(self):
        """De dikte van de trottoirband."""
        return self._dikte.waarde

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value)

    @property
    def vorm(self):
        """De vorm van de trottoirband."""
        return self._vorm.waarde

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTrottoirbandVorm(ComplexField, AttributeInfo):
    """Complex datatype voor de vorm van een trotoirband."""
    naam = 'DtcTrottoirbandVorm'
    label = 'Trottoirband vorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTrottoirbandVorm'
    definition = 'Complex datatype voor de vorm van een trotoirband.'
    waardeObject = DtcTrottoirbandVormWaarden

    def __str__(self):
        return ComplexField.__str__(self)

