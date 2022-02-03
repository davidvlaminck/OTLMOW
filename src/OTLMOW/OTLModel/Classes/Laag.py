# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlLaagRol import KlLaagRol
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Laag(AIMObject):
    """Abstracte voor de gemeenschappelijke eigenschappen van de onderliggende verhardings- en funderings-onderdelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.breedte',
                                     definition='De (gemiddelde) breedte van een laag in meter. Dit kan ook de nominale breedte zijn afhankelijk van de laag en situatie.',
                                     owner=self)

        self._laagRol = OTLAttribuut(field=KlLaagRol,
                                     naam='laagRol',
                                     label='laagrol',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.laagRol',
                                     definition='De functie die de laag vervult in de verticale opbouw.',
                                     owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.lengte',
                                    definition='De (gemiddelde) lengte van een laag in meter. Dit kan ook de nominale lengte zijn afhankelijk van de laag en situatie.',
                                    owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.oppervlakte',
                                         definition='De oppervlakte van een laag in vierkante meter.',
                                         owner=self)

    @property
    def breedte(self):
        """De (gemiddelde) breedte van een laag in meter. Dit kan ook de nominale breedte zijn afhankelijk van de laag en situatie."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def laagRol(self):
        """De functie die de laag vervult in de verticale opbouw."""
        return self._laagRol.waarde

    @laagRol.setter
    def laagRol(self, value):
        self._laagRol.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De (gemiddelde) lengte van een laag in meter. Dit kan ook de nominale lengte zijn afhankelijk van de laag en situatie."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De oppervlakte van een laag in vierkante meter."""
        return self._oppervlakte.waarde

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)
