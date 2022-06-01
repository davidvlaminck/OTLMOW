# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Classes.Sensoropstelling import Sensoropstelling
from OTLMOW.OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLMOW.OTLModel.Datatypes.KlNeerslagsensorMerk import KlNeerslagsensorMerk
from OTLMOW.OTLModel.Datatypes.KlNeerslagsensorModelnaam import KlNeerslagsensorModelnaam
from OTLMOW.OTLModel.Datatypes.KlNeerslagsensorType import KlNeerslagsensorType
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Neerslagsensor(AIMNaamObject, Sensoropstelling, PuntGeometrie):
    """Detectie van neerslag(hoeveelheid/intensiteit)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Neerslagsensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        Sensoropstelling.__init__(self)
        PuntGeometrie.__init__(self)

        self._dnsNaam = OTLAttribuut(field=StringField,
                                     naam='dnsNaam',
                                     label='DNS naam',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Neerslagsensor.dnsNaam',
                                     definition='De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.',
                                     owner=self)

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='ip adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Neerslagsensor.ipAdres',
                                     definition='IP-adres van de neerslagsensor.',
                                     owner=self)

        self._merk = OTLAttribuut(field=KlNeerslagsensorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Neerslagsensor.merk',
                                  definition='Het merk van de neerslagsensor.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlNeerslagsensorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Neerslagsensor.modelnaam',
                                       definition='De modelnaam van de neerslagsensor.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlNeerslagsensorType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Neerslagsensor.type',
                                  definition='Het type van de neerslagsensor.',
                                  owner=self)

    @property
    def dnsNaam(self):
        """De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""
        return self._dnsNaam.get_waarde()

    @dnsNaam.setter
    def dnsNaam(self, value):
        self._dnsNaam.set_waarde(value, owner=self)

    @property
    def ipAdres(self):
        """IP-adres van de neerslagsensor."""
        return self._ipAdres.get_waarde()

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van de neerslagsensor."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de neerslagsensor."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van de neerslagsensor."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
