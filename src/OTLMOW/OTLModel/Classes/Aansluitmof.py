# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.LinkendElement import LinkendElement
from OTLMOW.OTLModel.Datatypes.KlAansluitstukMateriaal import KlAansluitstukMateriaal
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aansluitmof(LinkendElement):
    """Aansluitingsstuk tussen 2 buizen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitmof'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._diameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitmof.diameter',
                                      definition='De diameter van het boorgat gebruikt door de aansluitmof  in millimeter.')

        self._materiaal = OTLAttribuut(field=KlAansluitstukMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitmof.materiaal',
                                       definition='Het materiaal van de aansluitmof.')

    @property
    def diameter(self):
        """De diameter van het boorgat gebruikt door de aansluitmof  in millimeter."""
        return self._diameter.waarde

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Het materiaal van de aansluitmof."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
