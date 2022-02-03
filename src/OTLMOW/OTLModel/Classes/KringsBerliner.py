# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlTypeBeschoeiing import KlTypeBeschoeiing
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class KringsBerliner(AIMObject, LijnGeometrie):
    """Een grond- en/of waterkerende constructie, die bestaat uit een verticaal in de grond geplaatste wand."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KringsBerliner'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        LijnGeometrie.__init__(self)

        self._beschoeiingsLengte = OTLAttribuut(field=KwantWrdInMeter,
                                                naam='beschoeiingsLengte',
                                                label='beschoeiingslengte',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KringsBerliner.beschoeiingsLengte',
                                                definition='De totale lengte van de beschoeiing langs de sleuf in lopende meter.',
                                                owner=self)

        self._buisdiepte = OTLAttribuut(field=KwantWrdInMeter,
                                        naam='buisdiepte',
                                        label='buisdiepte',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KringsBerliner.buisdiepte',
                                        definition='De diepte van de buis.',
                                        owner=self)

        self._type = OTLAttribuut(field=KlTypeBeschoeiing,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KringsBerliner.type',
                                  definition='Het type beschoeiing.',
                                  owner=self)

    @property
    def beschoeiingsLengte(self):
        """De totale lengte van de beschoeiing langs de sleuf in lopende meter."""
        return self._beschoeiingsLengte.waarde

    @beschoeiingsLengte.setter
    def beschoeiingsLengte(self, value):
        self._beschoeiingsLengte.set_waarde(value, owner=self)

    @property
    def buisdiepte(self):
        """De diepte van de buis."""
        return self._buisdiepte.waarde

    @buisdiepte.setter
    def buisdiepte(self, value):
        self._buisdiepte.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type beschoeiing."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
