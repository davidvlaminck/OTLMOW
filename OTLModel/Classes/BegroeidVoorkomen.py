# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcVegetatieSoortnaam import DtcVegetatieSoortnaam
from OTLModel.Datatypes.KlTaludWaarde import KlTaludWaarde
from OTLModel.Datatypes.KlVegetatieDrassigheid import KlVegetatieDrassigheid
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class BegroeidVoorkomen(AIMObject):
    """Abstracte die alle gemeenschappelijke eigenschappen omtrent begroeid voorkomen opsomt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen.breedte',
                                     definition='De afstand van het begroeide oppervlak dwars op de as van de (water)weg.')

        self._drassigheid = OTLAttribuut(field=KlVegetatieDrassigheid,
                                         naam='drassigheid',
                                         label='drassigheid',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen.drassigheid',
                                         definition='Mate waarin de bodem verzadigd is met water. De drassigheid geeft hierbij aan in welke mate de normale werking van types machines zou kunnen verstoord worden.')

        self._heeftObstakels = OTLAttribuut(field=BooleanField,
                                            naam='heeftObstakels',
                                            label='heeft obstakels',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen.heeftObstakels',
                                            definition='Eigenschap die aangeeft of er binnen het beheerdeel al dan niet objecten voorkomen die de vrije werking van machines of andere werktuigen kan verhinderen.')

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen.lengte',
                                    definition='De afstand van het begroeide oppervlak evenwijdig met de as van de (water)weg.')

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen.oppervlakte',
                                         definition='De oppervlakte van het begroeide oppervlak in vierkante meter.')

        self._soort = OTLAttribuut(field=DtcVegetatieSoortnaam,
                                   naam='soort',
                                   label='soort',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen.soort',
                                   kardinaliteit_max='*',
                                   definition='Met deze eigenschap worden de Nederlandse soortnaam, wetenschappelijke soortnaam en de soortcode van de meest voorkomende soorten binnen het begroeid oppervlak weergegeven.')

        self._taludwaarde = OTLAttribuut(field=KlTaludWaarde,
                                         naam='taludwaarde',
                                         label='taludwaarde',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen.taludwaarde',
                                         definition='Een talud is het kunstmatig gedeelte van een vlak van de wegbaan, dijken, spoorbanen, vestingswerken, ... dat een helling (min. 20%, max 80% voor kunstmatig verharde taluds) vertoont en bedoeld voor het opvangen van een hoogteverschil.')

    @property
    def breedte(self):
        """De afstand van het begroeide oppervlak dwars op de as van de (water)weg."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def drassigheid(self):
        """Mate waarin de bodem verzadigd is met water. De drassigheid geeft hierbij aan in welke mate de normale werking van types machines zou kunnen verstoord worden."""
        return self._drassigheid.waarde

    @drassigheid.setter
    def drassigheid(self, value):
        self._drassigheid.set_waarde(value, owner=self)

    @property
    def heeftObstakels(self):
        """Eigenschap die aangeeft of er binnen het beheerdeel al dan niet objecten voorkomen die de vrije werking van machines of andere werktuigen kan verhinderen."""
        return self._heeftObstakels.waarde

    @heeftObstakels.setter
    def heeftObstakels(self, value):
        self._heeftObstakels.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De afstand van het begroeide oppervlak evenwijdig met de as van de (water)weg."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De oppervlakte van het begroeide oppervlak in vierkante meter."""
        return self._oppervlakte.waarde

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def soort(self):
        """Met deze eigenschap worden de Nederlandse soortnaam, wetenschappelijke soortnaam en de soortcode van de meest voorkomende soorten binnen het begroeid oppervlak weergegeven."""
        return self._soort.waarde

    @soort.setter
    def soort(self, value):
        self._soort.set_waarde(value, owner=self)

    @property
    def taludwaarde(self):
        """Een talud is het kunstmatig gedeelte van een vlak van de wegbaan, dijken, spoorbanen, vestingswerken, ... dat een helling (min. 20%, max 80% voor kunstmatig verharde taluds) vertoont en bedoeld voor het opvangen van een hoogteverschil."""
        return self._taludwaarde.waarde

    @taludwaarde.setter
    def taludwaarde(self, value):
        self._taludwaarde.set_waarde(value, owner=self)
