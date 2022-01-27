# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLMOW.OTLModel.Datatypes.KlAudioTransportType import KlAudioTransportType
from OTLMOW.OTLModel.Datatypes.KlIntercomMerk import KlIntercomMerk
from OTLMOW.OTLModel.Datatypes.KlIntercomModelnaam import KlIntercomModelnaam
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class IntercomToestel(AIMNaamObject):
    """Het toestel dat deel uitmaakt van een intercomsysteem en audio- en/of videocommunicatie tussen twee personen mogelijk maakt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._dnsNaam = OTLAttribuut(field=StringField,
                                     naam='dnsNaam',
                                     label='DNS naam',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.dnsNaam',
                                     definition='De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.')

        self._heeftVideo = OTLAttribuut(field=BooleanField,
                                        naam='heeftVideo',
                                        label='heeft video',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.heeftVideo',
                                        definition='Geeft aan of communicatie tussen personen al dan niet via video kan verlopen.')

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='IP-adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.ipAdres',
                                     definition='Het IP-adres van het intercomtoestel.')

        self._merk = OTLAttribuut(field=KlIntercomMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.merk',
                                  definition='Het merk van het intercomtoestel.')

        self._modelnaam = OTLAttribuut(field=KlIntercomModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.modelnaam',
                                       definition='De modelnaam van het intercomtoestel.')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.technischeFiche',
                                             definition='De technische fiche van het intercomtoestel.')

        self._transportType = OTLAttribuut(field=KlAudioTransportType,
                                           naam='transportType',
                                           label='transporttype',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.transportType',
                                           definition='Geeft het type van (video- en) audiotransport aan van het intercomtoestel binnen het intercomsysteem.')

    @property
    def dnsNaam(self):
        """De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""
        return self._dnsNaam.waarde

    @dnsNaam.setter
    def dnsNaam(self, value):
        self._dnsNaam.set_waarde(value, owner=self)

    @property
    def heeftVideo(self):
        """Geeft aan of communicatie tussen personen al dan niet via video kan verlopen."""
        return self._heeftVideo.waarde

    @heeftVideo.setter
    def heeftVideo(self, value):
        self._heeftVideo.set_waarde(value, owner=self)

    @property
    def ipAdres(self):
        """Het IP-adres van het intercomtoestel."""
        return self._ipAdres.waarde

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van het intercomtoestel."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van het intercomtoestel."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van het intercomtoestel."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def transportType(self):
        """Geeft het type van (video- en) audiotransport aan van het intercomtoestel binnen het intercomsysteem."""
        return self._transportType.waarde

    @transportType.setter
    def transportType(self, value):
        self._transportType.set_waarde(value, owner=self)
