# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.LinkendElement import LinkendElement
from src.OTLMOW.OTLModel.Datatypes.KlAansluitstukMateriaal import KlAansluitstukMateriaal
from src.OTLMOW.OTLModel.Datatypes.KlHulpstukType import KlHulpstukType
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hulpstuk(LinkendElement):
    """Stukken die zorgen voor verbindingen tussen rechte buizen om bv. van richting te veranderen, te verlengen, te verlopen van diameter, meerdere buizen op mekaar aan te sluiten,..."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._inwendigeDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                               naam='inwendigeDiameter',
                                               label='inwendige diameter',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.inwendigeDiameter',
                                               definition='De diameter van de binnenzijde van het hulpstuk in millimeter.')

        self._materiaal = OTLAttribuut(field=KlAansluitstukMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.materiaal',
                                       definition='Het materiaal waaruit het hulpstuk vervaardigd is.')

        self._type = OTLAttribuut(field=KlHulpstukType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.type',
                                  definition='Het type van het hulpstuk.')

        self._uitwendigeDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                                naam='uitwendigeDiameter',
                                                label='uitwendige diameter',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.uitwendigeDiameter',
                                                definition='De diameter van de buitenzijde van het hulpstuk in millimeter.')

    @property
    def inwendigeDiameter(self):
        """De diameter van de binnenzijde van het hulpstuk in millimeter."""
        return self._inwendigeDiameter.waarde

    @inwendigeDiameter.setter
    def inwendigeDiameter(self, value):
        self._inwendigeDiameter.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Het materiaal waaruit het hulpstuk vervaardigd is."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van het hulpstuk."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def uitwendigeDiameter(self):
        """De diameter van de buitenzijde van het hulpstuk in millimeter."""
        return self._uitwendigeDiameter.waarde

    @uitwendigeDiameter.setter
    def uitwendigeDiameter(self, value):
        self._uitwendigeDiameter.set_waarde(value, owner=self)
