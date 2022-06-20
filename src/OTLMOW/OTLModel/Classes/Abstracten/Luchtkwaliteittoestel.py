# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.KlLuchtkwaliteitOpstellingMerk import KlLuchtkwaliteitOpstellingMerk
from OTLMOW.OTLModel.Datatypes.KlLuchtkwaliteitOpstellingModelnaam import KlLuchtkwaliteitOpstellingModelnaam
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Luchtkwaliteittoestel(AIMNaamObject, PuntGeometrie):
    """Abstracte voor attributen van onderdelen van de luchtkwaliteitsensor installatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Luchtkwaliteittoestel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._merk = OTLAttribuut(field=KlLuchtkwaliteitOpstellingMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Luchtkwaliteittoestel.merk',
                                  definition='Het merk van een onderdeel uit een luchtkwaliteitsinstallatie.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlLuchtkwaliteitOpstellingModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Luchtkwaliteittoestel.modelnaam',
                                       definition='De modelnaam van een onderdeel uit een luchtkwaliteitsinstallatie.',
                                       owner=self)

    @property
    def merk(self):
        """Het merk van een onderdeel uit een luchtkwaliteitsinstallatie."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van een onderdeel uit een luchtkwaliteitsinstallatie."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
