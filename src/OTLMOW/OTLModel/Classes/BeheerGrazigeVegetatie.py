# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcMaaien import DtcMaaien
from OTLMOW.OTLModel.Datatypes.KlBeheerGrazigeVegetatie import KlBeheerGrazigeVegetatie
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class BeheerGrazigeVegetatie(AIMObject):
    """Het beheerobject voor de grazige vegetatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._beheeroptie = OTLAttribuut(field=KlBeheerGrazigeVegetatie,
                                         naam='beheeroptie',
                                         label='beheeroptie',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie.beheeroptie',
                                         kardinaliteit_max='*',
                                         definition='Aanduiding van welk beheer wordt toegepast op de grazige vegetatie.',
                                         owner=self)

        self._heeftBeheerplan = OTLAttribuut(field=BooleanField,
                                             naam='heeftBeheerplan',
                                             label='heeft beheerplan',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie.heeftBeheerplan',
                                             definition='Aanduiding of er een beheerplan bestaat.',
                                             owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='Lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie.lengte',
                                    definition='De lengte in meter van de te behandelen grazige vegetatie.',
                                    owner=self)

        self._maaien = OTLAttribuut(field=DtcMaaien,
                                    naam='maaien',
                                    label='maaien',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie.maaien',
                                    definition='Complex datatype voor de eigenschappen van maaien.',
                                    owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie.oppervlakte',
                                         definition='De oppervlakte in vierkante meter van de te behandelen grazige vegetatie.',
                                         owner=self)

    @property
    def beheeroptie(self):
        """Aanduiding van welk beheer wordt toegepast op de grazige vegetatie."""
        return self._beheeroptie.get_waarde()

    @beheeroptie.setter
    def beheeroptie(self, value):
        self._beheeroptie.set_waarde(value, owner=self)

    @property
    def heeftBeheerplan(self):
        """Aanduiding of er een beheerplan bestaat."""
        return self._heeftBeheerplan.get_waarde()

    @heeftBeheerplan.setter
    def heeftBeheerplan(self, value):
        self._heeftBeheerplan.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De lengte in meter van de te behandelen grazige vegetatie."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def maaien(self):
        """Complex datatype voor de eigenschappen van maaien."""
        return self._maaien.get_waarde()

    @maaien.setter
    def maaien(self, value):
        self._maaien.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De oppervlakte in vierkante meter van de te behandelen grazige vegetatie."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)
