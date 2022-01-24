# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KlBeheerHoutigeVegetatie import KlBeheerHoutigeVegetatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BeheerHoutigeVegetatie(AIMObject):
    """Het beheerobject voor de houtige vegetatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerHoutigeVegetatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._beheeroptie = OTLAttribuut(field=KlBeheerHoutigeVegetatie,
                                         naam='beheeroptie',
                                         label='beheeroptie',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerHoutigeVegetatie.beheeroptie',
                                         kardinaliteit_max='*',
                                         definition='Aanduiding van welk beheer wordt toegepast op de houtige vegetatie.')

        self._heeftBeheerplan = OTLAttribuut(field=BooleanField,
                                             naam='heeftBeheerplan',
                                             label='heeft beheerplan',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerHoutigeVegetatie.heeftBeheerplan',
                                             definition='Aanduiding of er een beheerplan bestaat.')

    @property
    def beheeroptie(self):
        """Aanduiding van welk beheer wordt toegepast op de houtige vegetatie."""
        return self._beheeroptie.waarde

    @beheeroptie.setter
    def beheeroptie(self, value):
        self._beheeroptie.set_waarde(value, owner=self)

    @property
    def heeftBeheerplan(self):
        """Aanduiding of er een beheerplan bestaat."""
        return self._heeftBeheerplan.waarde

    @heeftBeheerplan.setter
    def heeftBeheerplan(self, value):
        self._heeftBeheerplan.set_waarde(value, owner=self)
