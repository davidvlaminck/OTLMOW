# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KlBeheerSierbeplanting import KlBeheerSierbeplanting
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class BeheerSierbeplanting(AIMObject):
    """Het beheerobject voor de sierbeplanting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerSierbeplanting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._beheeroptie = OTLAttribuut(field=KlBeheerSierbeplanting,
                                         naam='beheeroptie',
                                         label='beheeroptie',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerSierbeplanting.beheeroptie',
                                         kardinaliteit_max='*',
                                         definition='Aanduiding van welk beheer wordt toegepast op de sierbeplanting.')

        self._heeftBeheerplan = OTLAttribuut(field=BooleanField,
                                             naam='heeftBeheerplan',
                                             label='heeft beheerplan',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerSierbeplanting.heeftBeheerplan',
                                             definition='Aanduiding of er een beheerplan bestaat.')

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerSierbeplanting.oppervlakte',
                                         definition='De oppervlakte in vierkante meter van de te behandelen sierbeplanting.')

    @property
    def beheeroptie(self):
        """Aanduiding van welk beheer wordt toegepast op de sierbeplanting."""
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

    @property
    def oppervlakte(self):
        """De oppervlakte in vierkante meter van de te behandelen sierbeplanting."""
        return self._oppervlakte.waarde

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)
