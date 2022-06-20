# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.Abstracten.AfschermendeConstructie import AfschermendeConstructie
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class AansluitendeConstructie(AfschermendeConstructie, LijnGeometrie):
    """Abstracte die alle aansluitende constructies bundelt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AfschermendeConstructie.__init__(self)
        LijnGeometrie.__init__(self)

        self._totaleLengte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='totaleLengte',
                                          label='totale lengte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie.totaleLengte',
                                          definition='De totale lengte van de elementen van de aansluitende constructie.',
                                          owner=self)

    @property
    def totaleLengte(self):
        """De totale lengte van de elementen van de aansluitende constructie."""
        return self._totaleLengte.get_waarde()

    @totaleLengte.setter
    def totaleLengte(self, value):
        self._totaleLengte.set_waarde(value, owner=self)
