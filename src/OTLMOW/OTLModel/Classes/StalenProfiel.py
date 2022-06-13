# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.ConstructieElement import ConstructieElement
from OTLMOW.OTLModel.Classes.ConstructieElementenGC import ConstructieElementenGC
from OTLMOW.OTLModel.Classes.StalenConstructieElement import StalenConstructieElement
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class StalenProfiel(ConstructieElement, ConstructieElementenGC, StalenConstructieElement):
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
                                           definition='Bij het fabriceren wordt er bewust een ronding aangebracht in het profiel. Dit kan bijvoorbeeld dienen ter compensatie van doorbuiging of omwille van esthetische redenen,...',
                                           owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel.lengte',
                                    definition='De lengte van het profiel uitgedrukt in in meter.',
                                    owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel.technischeFiche',
                                             definition='De technische gegevens van het stalen profiel (relevante normen, detail afmetingen, gewicht,...).',
                                             owner=self)

    @property
    def isVoorgebogen(self):
        """Bij het fabriceren wordt er bewust een ronding aangebracht in het profiel. Dit kan bijvoorbeeld dienen ter compensatie van doorbuiging of omwille van esthetische redenen,..."""
        return self._isVoorgebogen.get_waarde()

    @isVoorgebogen.setter
    def isVoorgebogen(self, value):
        self._isVoorgebogen.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De lengte van het profiel uitgedrukt in in meter."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische gegevens van het stalen profiel (relevante normen, detail afmetingen, gewicht,...)."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
