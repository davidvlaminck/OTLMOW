# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KlVerkeerslichtMasker import KlVerkeerslichtMasker
from OTLModel.Datatypes.KlVerkeerslichtMerk import KlVerkeerslichtMerk
from OTLModel.Datatypes.KlVerkeerslichtModelnaam import KlVerkeerslichtModelnaam
from OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeerslicht(AIMNaamObject):
    """Abstracte voor verkeerslichten. Dit zijn apparaten, opgesteld naast of boven de weg, om weggebruikers visueel te geleiden over een kruispunt door het gebruik van rode, oranje-gele en groene lichten. De bepalingen van de wegcode zijn van toepassing, meer bepaald titel III, hoofdstuk I, artikelen 61 t.e.m. 64."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeerslicht'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._masker = OTLAttribuut(field=KlVerkeerslichtMasker,
                                    naam='masker',
                                    label='masker',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeerslicht.masker',
                                    definition='Type masker dat is aangebracht op het verkeerslicht.')

        self._merk = OTLAttribuut(field=KlVerkeerslichtMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeerslicht.merk',
                                  definition='Het merk van het verkeerslicht.')

        self._modelnaam = OTLAttribuut(field=KlVerkeerslichtModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeerslicht.modelnaam',
                                       definition='De modelnaam/product range van het verkeerslicht.')

        self._vermogen = OTLAttribuut(field=KwantWrdInWatt,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeerslicht.vermogen',
                                      definition='Vermogen (Watt) van het verkeerslicht.')

    @property
    def masker(self):
        """Type masker dat is aangebracht op het verkeerslicht."""
        return self._masker.waarde

    @masker.setter
    def masker(self, value):
        self._masker.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van het verkeerslicht."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam/product range van het verkeerslicht."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def vermogen(self):
        """Vermogen (Watt) van het verkeerslicht."""
        return self._vermogen.waarde

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)
