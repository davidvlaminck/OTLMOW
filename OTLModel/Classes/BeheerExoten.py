# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KlBeheerExoten import KlBeheerExoten
from OTLModel.Datatypes.KlNazorgJaarfrequentie import KlNazorgJaarfrequentie
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class BeheerExoten(AIMObject, AttributeInfo):
    """Het beheerobject voor de exoten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)

        self._beheeroptie = OTLAttribuut(field=KlBeheerExoten,
                                         naam='beheeroptie',
                                         label='beheeroptie',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.beheeroptie',
                                         definition='Behandelingswijzen van exoten.')

        self._bijzondereAfvoerVereist = OTLAttribuut(field=BooleanField,
                                                     naam='bijzondereAfvoerVereist',
                                                     label='bijzondere afvoer vereist',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.bijzondereAfvoerVereist',
                                                     definition='Aanduiding of voor de verwijderde exoten een niet-reguliere afvoer is voorzien.')

        self._heeftDeponie = OTLAttribuut(field=BooleanField,
                                          naam='heeftDeponie',
                                          label='heeft deponie',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.heeftDeponie',
                                          definition='Aanduiding of de Japanse duizendknoop terplaatse kan worden gedeponeerd in een gecontamineerde zone.')

        self._nazorgJaarfrequentie = OTLAttribuut(field=KlNazorgJaarfrequentie,
                                                  naam='nazorgJaarfrequentie',
                                                  label='nazorg jaarfrequentie',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.nazorgJaarfrequentie',
                                                  definition='Aantal keer dat de behandelde zone jaarlijks dient te worden gecontroleerd.')

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.oppervlakte',
                                         definition='De oppervlakte in vierkante meter van de te behandelen exoten.')

    @property
    def beheeroptie(self):
        """Behandelingswijzen van exoten."""
        return self._beheeroptie.waarde

    @beheeroptie.setter
    def beheeroptie(self, value):
        self._beheeroptie.set_waarde(value, owner=self)

    @property
    def bijzondereAfvoerVereist(self):
        """Aanduiding of voor de verwijderde exoten een niet-reguliere afvoer is voorzien."""
        return self._bijzondereAfvoerVereist.waarde

    @bijzondereAfvoerVereist.setter
    def bijzondereAfvoerVereist(self, value):
        self._bijzondereAfvoerVereist.set_waarde(value, owner=self)

    @property
    def heeftDeponie(self):
        """Aanduiding of de Japanse duizendknoop terplaatse kan worden gedeponeerd in een gecontamineerde zone."""
        return self._heeftDeponie.waarde

    @heeftDeponie.setter
    def heeftDeponie(self, value):
        self._heeftDeponie.set_waarde(value, owner=self)

    @property
    def nazorgJaarfrequentie(self):
        """Aantal keer dat de behandelde zone jaarlijks dient te worden gecontroleerd."""
        return self._nazorgJaarfrequentie.waarde

    @nazorgJaarfrequentie.setter
    def nazorgJaarfrequentie(self, value):
        self._nazorgJaarfrequentie.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De oppervlakte in vierkante meter van de te behandelen exoten."""
        return self._oppervlakte.waarde

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)
