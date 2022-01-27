# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from src.OTLMOW.OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from src.OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class MIVProcessorkaart(AIMNaamObject):
    """Meten in Vlaanderen : processorkaart van de lokale verwerkingseenheid."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVProcessorkaart'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._dnsNaam = OTLAttribuut(field=StringField,
                                     naam='dnsNaam',
                                     label='DNS naam',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVProcessorkaart.dnsNaam',
                                     definition='De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.')

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='ip adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVProcessorkaart.ipAdres',
                                     definition='IP-adres van de MIV-processorkaart.')

        self._softwareversie = OTLAttribuut(field=StringField,
                                            naam='softwareversie',
                                            label='softwareversie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVProcessorkaart.softwareversie',
                                            definition='De opsomming van de verschillende software-patches.')

    @property
    def dnsNaam(self):
        """De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""
        return self._dnsNaam.waarde

    @dnsNaam.setter
    def dnsNaam(self, value):
        self._dnsNaam.set_waarde(value, owner=self)

    @property
    def ipAdres(self):
        """IP-adres van de MIV-processorkaart."""
        return self._ipAdres.waarde

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def softwareversie(self):
        """De opsomming van de verschillende software-patches."""
        return self._softwareversie.waarde

    @softwareversie.setter
    def softwareversie(self, value):
        self._softwareversie.set_waarde(value, owner=self)
