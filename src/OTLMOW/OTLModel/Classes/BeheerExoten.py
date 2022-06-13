# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KlBeheerExoten import KlBeheerExoten
from OTLMOW.OTLModel.Datatypes.KlNazorgJaarfrequentie import KlNazorgJaarfrequentie
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class BeheerExoten(AIMObject):
    """Het beheerobject voor de exoten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._beheeroptie = OTLAttribuut(field=KlBeheerExoten,
                                         naam='beheeroptie',
                                         label='beheeroptie',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.beheeroptie',
                                         definition='Behandelingswijzen van exoten.',
                                         owner=self)

        self._bijzondereAfvoerVereist = OTLAttribuut(field=BooleanField,
                                                     naam='bijzondereAfvoerVereist',
                                                     label='bijzondere afvoer vereist',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.bijzondereAfvoerVereist',
                                                     definition='Aanduiding of voor de verwijderde exoten een niet-reguliere afvoer is voorzien.',
                                                     owner=self)

        self._heeftDeponie = OTLAttribuut(field=BooleanField,
                                          naam='heeftDeponie',
                                          label='heeft deponie',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.heeftDeponie',
                                          definition='Aanduiding of de Japanse duizendknoop terplaatse kan worden gedeponeerd in een gecontamineerde zone.',
                                          owner=self)

        self._nazorgJaarfrequentie = OTLAttribuut(field=KlNazorgJaarfrequentie,
                                                  naam='nazorgJaarfrequentie',
                                                  label='nazorg jaarfrequentie',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.nazorgJaarfrequentie',
                                                  definition='Aantal keer dat de behandelde zone jaarlijks dient te worden gecontroleerd.',
                                                  owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.oppervlakte',
                                         definition='De oppervlakte in vierkante meter van de te behandelen exoten.',
                                         owner=self)

    @property
    def beheeroptie(self):
        """Behandelingswijzen van exoten."""
        return self._beheeroptie.get_waarde()

    @beheeroptie.setter
    def beheeroptie(self, value):
        self._beheeroptie.set_waarde(value, owner=self)

    @property
    def bijzondereAfvoerVereist(self):
        """Aanduiding of voor de verwijderde exoten een niet-reguliere afvoer is voorzien."""
        return self._bijzondereAfvoerVereist.get_waarde()

    @bijzondereAfvoerVereist.setter
    def bijzondereAfvoerVereist(self, value):
        self._bijzondereAfvoerVereist.set_waarde(value, owner=self)

    @property
    def heeftDeponie(self):
        """Aanduiding of de Japanse duizendknoop terplaatse kan worden gedeponeerd in een gecontamineerde zone."""
        return self._heeftDeponie.get_waarde()

    @heeftDeponie.setter
    def heeftDeponie(self, value):
        self._heeftDeponie.set_waarde(value, owner=self)

    @property
    def nazorgJaarfrequentie(self):
        """Aantal keer dat de behandelde zone jaarlijks dient te worden gecontroleerd."""
        return self._nazorgJaarfrequentie.get_waarde()

    @nazorgJaarfrequentie.setter
    def nazorgJaarfrequentie(self, value):
        self._nazorgJaarfrequentie.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De oppervlakte in vierkante meter van de te behandelen exoten."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)
