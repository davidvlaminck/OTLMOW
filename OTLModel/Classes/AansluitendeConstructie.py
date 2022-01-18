# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.AfschermendeConstructie import AfschermendeConstructie
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class AansluitendeConstructie(AfschermendeConstructie, AttributeInfo):
    """Abstracte die alle aansluitende constructies bundelt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AfschermendeConstructie.__init__(self)
        AttributeInfo.__init__(self)

        self._totaleLengte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='totaleLengte',
                                          label='totale lengte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie.totaleLengte',
                                          definition='De totale lengte van de elementen van de aansluitende constructie.')

    @property
    def totaleLengte(self):
        """De totale lengte van de elementen van de aansluitende constructie."""
        return self._totaleLengte.waarde

    @totaleLengte.setter
    def totaleLengte(self, value):
        self._totaleLengte.set_waarde(value, owner=self)
