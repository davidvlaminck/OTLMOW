# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from src.OTLMOW.OTLModel.Datatypes.KlBouwputType import KlBouwputType
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bouwput(AIMObject):
    """De ontgraving die nodig is voor het maken van een ondergrondse constructie zoals bv. een put of putten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bouwput'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._putdiepte = OTLAttribuut(field=KwantWrdInMeter,
                                       naam='putdiepte',
                                       label='putdiepte',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bouwput.putdiepte',
                                       definition='Diepte tussen het maaiveld en onderkant bouwput in meter.')

        self._type = OTLAttribuut(field=KlBouwputType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bouwput.type',
                                  definition='Het type van bouwput.')

    @property
    def putdiepte(self):
        """Diepte tussen het maaiveld en onderkant bouwput in meter."""
        return self._putdiepte.waarde

    @putdiepte.setter
    def putdiepte(self, value):
        self._putdiepte.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van bouwput."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
