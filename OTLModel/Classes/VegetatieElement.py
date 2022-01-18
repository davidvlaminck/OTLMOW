# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.DtcVegetatieSoortnaam import DtcVegetatieSoortnaam
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.KlVegetatieelementHoogte import KlVegetatieelementHoogte


# Generated with OTLClassCreator. To modify: extend, do not edit
class VegetatieElement(AIMObject, AttributeInfo):
    """Abstracte om alle gemeenschappelijke eigenschappen en relaties van de solitaire plant in de ruimte onder 1 noemer te plaatsen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)

        self._hoogte = OTLAttribuut(field=KlVegetatieelementHoogte,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement.hoogte',
                                    definition='De hoogteklasse van het vegetatie-element.')

        self._niveau = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='niveau',
                                    label='niveau',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement.niveau',
                                    definition='Het niveau waarop het object zich bevindt, relatief ten opzichte van andere objecten. Negatieve waarden worden geassocieerd met ondergronds en positieve waarden met bovengronds. Nul wordt beschouwd als een absolute waarde om het maaiveld aan te duiden.')

        self._soortnaam = OTLAttribuut(field=DtcVegetatieSoortnaam,
                                       naam='soortnaam',
                                       label='soortnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement.soortnaam',
                                       definition='Met deze eigenschap worden de Nederlandse soortnaam, wetenschappelijke soortnaam en de soortcode van de plantensoort weergegeven.')

    @property
    def hoogte(self):
        """De hoogteklasse van het vegetatie-element."""
        return self._hoogte.waarde

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def niveau(self):
        """Het niveau waarop het object zich bevindt, relatief ten opzichte van andere objecten. Negatieve waarden worden geassocieerd met ondergronds en positieve waarden met bovengronds. Nul wordt beschouwd als een absolute waarde om het maaiveld aan te duiden."""
        return self._niveau.waarde

    @niveau.setter
    def niveau(self, value):
        self._niveau.set_waarde(value, owner=self)

    @property
    def soortnaam(self):
        """Met deze eigenschap worden de Nederlandse soortnaam, wetenschappelijke soortnaam en de soortcode van de plantensoort weergegeven."""
        return self._soortnaam.waarde

    @soortnaam.setter
    def soortnaam(self, value):
        self._soortnaam.set_waarde(value, owner=self)
