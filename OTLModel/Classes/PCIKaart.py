# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KlPCIkaartMerk import KlPCIkaartMerk
from OTLModel.Datatypes.KlPCIkaartModelnaam import KlPCIkaartModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class PCIKaart(AIMNaamObject, AttributeInfo):
    """Peripheral Component Interconnect of uitbreidingssleuf."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PCIKaart'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        AttributeInfo.__init__(self)

        self._merk = OTLAttribuut(field=KlPCIkaartMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PCIKaart.merk',
                                  definition='Het merk van de PCI-kaart.')

        self._modelnaam = OTLAttribuut(field=KlPCIkaartModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PCIKaart.modelnaam',
                                       definition='De modelnaam van de PCI-kaart.')

    @property
    def merk(self):
        """Het merk van de PCI-kaart."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de PCI-kaart."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
