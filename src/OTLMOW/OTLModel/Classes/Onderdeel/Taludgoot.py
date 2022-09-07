# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlTaludgootType import KlTaludgootType
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Taludgoot(AIMObject, LijnGeometrie):
    """Goot die in het talud loodrecht op de kruinlijn is aangebracht. De functie hiervan is onder meer opvang en afvoer hemelwater."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taludgoot'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement')

        self._totaleLengte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='totaleLengte',
                                          label='totale lengte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taludgoot.totaleLengte',
                                          definition='De totale lengte van de geprefabriceerde betonelementen in lopende meter vanaf het beginstuk (niet inbegrepen) tot aan het eindstuk (niet inbegrepen).',
                                          owner=self)

        self._type = OTLAttribuut(field=KlTaludgootType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taludgoot.type',
                                  definition='Het type van geprefabriceerd betonelement.',
                                  owner=self)

    @property
    def totaleLengte(self):
        """De totale lengte van de geprefabriceerde betonelementen in lopende meter vanaf het beginstuk (niet inbegrepen) tot aan het eindstuk (niet inbegrepen)."""
        return self._totaleLengte.get_waarde()

    @totaleLengte.setter
    def totaleLengte(self, value):
        self._totaleLengte.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van geprefabriceerd betonelement."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
