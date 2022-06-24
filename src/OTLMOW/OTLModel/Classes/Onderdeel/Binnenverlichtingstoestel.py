# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlBinnenverlichtingstoestelSchakelwijze import KlBinnenverlichtingstoestelSchakelwijze
from OTLMOW.OTLModel.Datatypes.KlBinnenverlichtingstoestelSoortLamp import KlBinnenverlichtingstoestelSoortLamp
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Binnenverlichtingstoestel(AIMObject, PuntGeometrie):
    """Een verlichtingstoestel dat binnen in een gebouw geplaatst wordt. Een verlichtingstoestel is de combinatie van de lamp en de armatuur."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._schakelwijze = OTLAttribuut(field=KlBinnenverlichtingstoestelSchakelwijze,
                                          naam='schakelwijze',
                                          label='schakelwijze',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel.schakelwijze',
                                          definition='Geeft aan hoe het toestel aan- en uitgeschakeld wordt.',
                                          owner=self)

        self._soortLamp = OTLAttribuut(field=KlBinnenverlichtingstoestelSoortLamp,
                                       naam='soortLamp',
                                       label='soort lamp',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel.soortLamp',
                                       definition='Geeft aan welke soort lamp er gebruikt wordt in het binnenverlichtingstoestel.',
                                       owner=self)

    @property
    def schakelwijze(self):
        """Geeft aan hoe het toestel aan- en uitgeschakeld wordt."""
        return self._schakelwijze.get_waarde()

    @schakelwijze.setter
    def schakelwijze(self, value):
        self._schakelwijze.set_waarde(value, owner=self)

    @property
    def soortLamp(self):
        """Geeft aan welke soort lamp er gebruikt wordt in het binnenverlichtingstoestel."""
        return self._soortLamp.get_waarde()

    @soortLamp.setter
    def soortLamp(self, value):
        self._soortLamp.set_waarde(value, owner=self)
