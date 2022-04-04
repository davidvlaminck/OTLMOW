# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KlVerlichtingstoestelMerk import KlVerlichtingstoestelMerk
from OTLMOW.OTLModel.Datatypes.KlVerlichtingstoestelModelnaam import KlVerlichtingstoestelModelnaam
from OTLMOW.OTLModel.Datatypes.KlVerlichtingstoestelVerlichtGebied import KlVerlichtingstoestelVerlichtGebied
from OTLMOW.OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verlichtingstoestel(AIMNaamObject, PuntGeometrie):
    """Abstracte voor het geheel van de lichtbron en de behuizing die werden samengesteld met als doel:
* de lichtstroom van de lichtbronnen hoofdzakelijk op het te verlichten oppervlak (doorlopende wegsectie, conflictgebied,...) te richten, teneinde de zichtbaarheid te verhogen;
* de lichtstroom te beheersen zodat de weggebruikers niet verblind worden en de lichthinder beperkt wordt;
* het optisch systeem, de lichtbronnen en de hulpapparatuur tegen uitwendige invloeden te beschermen"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._heeftAansluitkastGeintegreerd = OTLAttribuut(field=BooleanField,
                                                           naam='heeftAansluitkastGeintegreerd',
                                                           label='heeft aansluitkast geïntegreerd',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.heeftAansluitkastGeintegreerd',
                                                           definition='Is de aansluitkast geïntegreerd?',
                                                           owner=self)

        self._merk = OTLAttribuut(field=KlVerlichtingstoestelMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.merk',
                                  definition='Het merk van het verlichtingstoestel.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlVerlichtingstoestelModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.modelnaam',
                                       definition='De modelnaam van het verlichtingstoestel.',
                                       owner=self)

        self._stroomkringnummer = OTLAttribuut(field=StringField,
                                               naam='stroomkringnummer',
                                               label='stroomkringnummer',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.stroomkringnummer',
                                               definition='Nummer van de stroomkring waarop het verlichtingstoestel is aangesloten.',
                                               owner=self)

        self._systeemvermogen = OTLAttribuut(field=KwantWrdInWatt,
                                             naam='systeemvermogen',
                                             label='systeemvermogen',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.systeemvermogen',
                                             definition='Systeemvermogen (Watt) van het verlichtingstoestel.',
                                             owner=self)

        self._verlichtGebied = OTLAttribuut(field=KlVerlichtingstoestelVerlichtGebied,
                                            naam='verlichtGebied',
                                            label='verlicht gebied',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.verlichtGebied',
                                            definition='Het gebied op de wegbaan of het object dat verlicht wordt door het verlichtingstoestel.',
                                            owner=self)

    @property
    def heeftAansluitkastGeintegreerd(self):
        """Is de aansluitkast geïntegreerd?"""
        return self._heeftAansluitkastGeintegreerd.waarde

    @heeftAansluitkastGeintegreerd.setter
    def heeftAansluitkastGeintegreerd(self, value):
        self._heeftAansluitkastGeintegreerd.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van het verlichtingstoestel."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van het verlichtingstoestel."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def stroomkringnummer(self):
        """Nummer van de stroomkring waarop het verlichtingstoestel is aangesloten."""
        return self._stroomkringnummer.waarde

    @stroomkringnummer.setter
    def stroomkringnummer(self, value):
        self._stroomkringnummer.set_waarde(value, owner=self)

    @property
    def systeemvermogen(self):
        """Systeemvermogen (Watt) van het verlichtingstoestel."""
        return self._systeemvermogen.waarde

    @systeemvermogen.setter
    def systeemvermogen(self, value):
        self._systeemvermogen.set_waarde(value, owner=self)

    @property
    def verlichtGebied(self):
        """Het gebied op de wegbaan of het object dat verlicht wordt door het verlichtingstoestel."""
        return self._verlichtGebied.waarde

    @verlichtGebied.setter
    def verlichtGebied(self, value):
        self._verlichtGebied.set_waarde(value, owner=self)
