# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from src.OTLMOW.OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from src.OTLMOW.OTLModel.Datatypes.KlIpPowerSwitchType import KlIpPowerSwitchType
from src.OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class IpPowerSwitch(AIMNaamObject):
    """Een IP powerswitch levert netspanning (230V) aan achterliggende apparaten. Door in te loggen op de powerswitch kunt u de poort en dus de netspanning naar het aangesloten apparaat vanop afstand uit en aan zetten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IpPowerSwitch'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._dnsNaam = OTLAttribuut(field=StringField,
                                     naam='dnsNaam',
                                     label='DNS naam',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IpPowerSwitch.dnsNaam',
                                     definition='De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.')

        self._handleiding = OTLAttribuut(field=DtcDocument,
                                         naam='handleiding',
                                         label='handleiding',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IpPowerSwitch.handleiding',
                                         usagenote='Bestanden van het type pdf.',
                                         definition='De handleiding van de IP powerswitch.')

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='ip adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IpPowerSwitch.ipAdres',
                                     definition='Het IP-adres van de IP power switch.')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IpPowerSwitch.technischeFiche',
                                             usagenote='Bestanden van het type pdf.',
                                             definition='De technische fiche  van de IP powerswitch.')

        self._type = OTLAttribuut(field=KlIpPowerSwitchType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IpPowerSwitch.type',
                                  definition='Merk en type van de IP powerswitch.')

    @property
    def dnsNaam(self):
        """De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""
        return self._dnsNaam.waarde

    @dnsNaam.setter
    def dnsNaam(self, value):
        self._dnsNaam.set_waarde(value, owner=self)

    @property
    def handleiding(self):
        """De handleiding van de IP powerswitch."""
        return self._handleiding.waarde

    @handleiding.setter
    def handleiding(self, value):
        self._handleiding.set_waarde(value, owner=self)

    @property
    def ipAdres(self):
        """Het IP-adres van de IP power switch."""
        return self._ipAdres.waarde

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche  van de IP powerswitch."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def type(self):
        """Merk en type van de IP powerswitch."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
