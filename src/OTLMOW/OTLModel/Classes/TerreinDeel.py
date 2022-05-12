# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class TerreinDeel(ABC):
    """Abstracte voor het gedeelte van het aardoppervlak, met een gelijkaardige functie, dat geen deel uitmaakt van 'waterdeel'."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TerreinDeel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TerreinDeel.breedte',
                                     definition='De breedte van het object in meter. In geval van een ongelijkmatige breedte wordt de gemiddelde breedte opgenomen.',
                                     owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TerreinDeel.lengte',
                                    definition='De lengte van het object in meter. In geval van een ongelijkmatige lengte wordt de gemiddelde lengte opgenomen.',
                                    owner=self)

        self._niveau = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='niveau',
                                    label='niveau',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TerreinDeel.niveau',
                                    definition='Het niveau waarop het object zich bevindt, relatief ten opzichte van andere objecten. Negatieve waarden worden geassocieerd met ondergronds en positieve waarden met bovengronds. Nul wordt beschouwd als een absolute waarde om het maaiveld aan te duiden.',
                                    owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TerreinDeel.oppervlakte',
                                         definition='De oppervlakte in vierkante meter.',
                                         owner=self)

    @property
    def breedte(self):
        """De breedte van het object in meter. In geval van een ongelijkmatige breedte wordt de gemiddelde breedte opgenomen."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De lengte van het object in meter. In geval van een ongelijkmatige lengte wordt de gemiddelde lengte opgenomen."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def niveau(self):
        """Het niveau waarop het object zich bevindt, relatief ten opzichte van andere objecten. Negatieve waarden worden geassocieerd met ondergronds en positieve waarden met bovengronds. Nul wordt beschouwd als een absolute waarde om het maaiveld aan te duiden."""
        return self._niveau.get_waarde()

    @niveau.setter
    def niveau(self, value):
        self._niveau.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De oppervlakte in vierkante meter."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)
