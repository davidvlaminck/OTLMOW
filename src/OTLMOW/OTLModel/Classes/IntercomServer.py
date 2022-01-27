# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from src.OTLMOW.OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from src.OTLMOW.OTLModel.Datatypes.KlAudioTransportType import KlAudioTransportType
from src.OTLMOW.OTLModel.Datatypes.KlIntercomServerMerk import KlIntercomServerMerk
from src.OTLMOW.OTLModel.Datatypes.KlIntercomServerModelnaam import KlIntercomServerModelnaam
from src.OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class IntercomServer(AIMNaamObject):
    """Centrale module - inclusief configuratiesoftware - die de intercomtoestellen koppelt, bv. per tunnel of per complex, en een gateway opzet naar de centrale systemen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._dnsNaam = OTLAttribuut(field=StringField,
                                     naam='dnsNaam',
                                     label='DNS naam',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer.dnsNaam',
                                     definition='De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.')

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='IP-adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer.ipAdres',
                                     definition='Het IP-adres van de intercomserver.')

        self._merk = OTLAttribuut(field=KlIntercomServerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer.merk',
                                  definition='Het merk van de intercomserver.')

        self._modelnaam = OTLAttribuut(field=KlIntercomServerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer.modelnaam',
                                       definition='De modelnaam van de intercomserver.')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer.technischeFiche',
                                             definition='De technische fiche van de intercomserver.')

        self._transportType = OTLAttribuut(field=KlAudioTransportType,
                                           naam='transportType',
                                           label='transport type',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer.transportType',
                                           definition='Geeft aan op welke manier het audiosignaal wordt getransporteerd door het toestel.')

    @property
    def dnsNaam(self):
        """De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""
        return self._dnsNaam.waarde

    @dnsNaam.setter
    def dnsNaam(self, value):
        self._dnsNaam.set_waarde(value, owner=self)

    @property
    def ipAdres(self):
        """Het IP-adres van de intercomserver."""
        return self._ipAdres.waarde

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van de intercomserver."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de intercomserver."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de intercomserver."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def transportType(self):
        """Geeft aan op welke manier het audiosignaal wordt getransporteerd door het toestel."""
        return self._transportType.waarde

    @transportType.setter
    def transportType(self, value):
        self._transportType.set_waarde(value, owner=self)
