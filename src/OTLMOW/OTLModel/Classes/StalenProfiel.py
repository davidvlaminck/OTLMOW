# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from src.OTLMOW.OTLModel.Classes.ConstructieElement import ConstructieElement
from src.OTLMOW.OTLModel.Classes.StalenConstructieElement import StalenConstructieElement
from src.OTLMOW.OTLModel.Classes.ConstructieElementenGC import ConstructieElementenGC
from src.OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class StalenProfiel(ConstructieElement, StalenConstructieElement, ConstructieElementenGC):
    """Bundeling van gemeenschappelijke eigenschappen van standaard en niet-standaard stalen profiel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        ConstructieElement.__init__(self)
        ConstructieElementenGC.__init__(self)
        StalenConstructieElement.__init__(self)

        self._isVoorgebogen = OTLAttribuut(field=BooleanField,
                                           naam='isVoorgebogen',
                                           label='is voorgebogen',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel.isVoorgebogen',
                                           definition='Bij het fabriceren wordt er bewust een ronding aangebracht in het profiel. Dit kan bijvoorbeeld dienen ter compensatie van doorbuiging of omwille van esthetische redenen,...')

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel.lengte',
                                    definition='De lengte van het profiel uitgedrukt in in meter.')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel.technischeFiche',
                                             definition='De technische gegevens van het stalen profiel (relevante normen, detail afmetingen, gewicht,...).')

    @property
    def isVoorgebogen(self):
        """Bij het fabriceren wordt er bewust een ronding aangebracht in het profiel. Dit kan bijvoorbeeld dienen ter compensatie van doorbuiging of omwille van esthetische redenen,..."""
        return self._isVoorgebogen.waarde

    @isVoorgebogen.setter
    def isVoorgebogen(self, value):
        self._isVoorgebogen.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De lengte van het profiel uitgedrukt in in meter."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische gegevens van het stalen profiel (relevante normen, detail afmetingen, gewicht,...)."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
