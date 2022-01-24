# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KlPTRegelaarModuleMerk import KlPTRegelaarModuleMerk
from OTLModel.Datatypes.KlPTRegelaarModuleModelnaam import KlPTRegelaarModuleModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTRegelaarModule(AIMNaamObject):
    """Abstracte voor de verschillende modules waaruit het personentransportbeïnvloedingssysteem van de verkeersregelaar opgebouwd is. Hierdoor zal het personentransport een snellere doorstroming aan een verkeerslichtengeregeld kruispunt genieten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PTRegelaarModule'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlPTRegelaarModuleMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PTRegelaarModule.merk',
                                  definition='Het merk van de PT regelaar module.')

        self._modelnaam = OTLAttribuut(field=KlPTRegelaarModuleModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PTRegelaarModule.modelnaam',
                                       definition='De modelnaam/product range van de PT regelaar module.')

    @property
    def merk(self):
        """Het merk van de PT regelaar module."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam/product range van de PT regelaar module."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
