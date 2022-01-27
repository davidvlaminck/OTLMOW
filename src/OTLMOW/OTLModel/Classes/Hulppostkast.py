# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Buitenkast import Buitenkast
from OTLMOW.OTLModel.Datatypes.KlHulppostkastType import KlHulppostkastType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hulppostkast(Buitenkast):
    """Een kast waarin verschillende onderdelen verzameld worden voor bijstand in noodgevallen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulppostkast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._type = OTLAttribuut(field=KlHulppostkastType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulppostkast.type',
                                  definition='Classificatie van de hulppostkast op basis van de inhoud en vorm volgens gangbare standaarden.')

    @property
    def type(self):
        """Classificatie van de hulppostkast op basis van de inhoud en vorm volgens gangbare standaarden."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
