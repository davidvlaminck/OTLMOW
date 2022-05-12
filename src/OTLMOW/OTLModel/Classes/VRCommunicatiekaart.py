# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.VRModuleMetFirmware import VRModuleMetFirmware
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLMOW.OTLModel.Datatypes.KlVrComKaartTypeOpslaggeheugen import KlVrComKaartTypeOpslaggeheugen
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRCommunicatiekaart(VRModuleMetFirmware):
    """Modem die alle toestandswijzigingen van de stuurkaart doorgeeft aan het afstandsbewakingssysteem. De module maakt continue een backup van alle log en data gegevens en slaat deze op op de aanwezige SD kaart. Tevens wordt de module ook gebruikt om vanop afstand te kunnen communiceren met de regelaar"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRCommunicatiekaart'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._dnsNaam = OTLAttribuut(field=StringField,
                                     naam='dnsNaam',
                                     label='DNS naam',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRCommunicatiekaart.dnsNaam',
                                     definition='De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.',
                                     owner=self)

        self._heeftSmartguard = OTLAttribuut(field=BooleanField,
                                             naam='heeftSmartguard',
                                             label='heeft smartguard',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRCommunicatiekaart.heeftSmartguard',
                                             definition='Smartguard aanwezig?',
                                             owner=self)

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='ipv4 adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRCommunicatiekaart.ipAdres',
                                     definition='IP-adres.',
                                     owner=self)

        self._telefoonnummer = OTLAttribuut(field=StringField,
                                            naam='telefoonnummer',
                                            label='telefoonnummer',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRCommunicatiekaart.telefoonnummer',
                                            definition='Telefoonnummer.',
                                            owner=self)

        self._typeGeheugen = OTLAttribuut(field=KlVrComKaartTypeOpslaggeheugen,
                                          naam='typeGeheugen',
                                          label='type geheugen',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRCommunicatiekaart.typeGeheugen',
                                          definition='Type opslaggeheugen op de aanwezige SD-kaart.',
                                          owner=self)

        self._uitvoering = OTLAttribuut(field=StringField,
                                        naam='uitvoering',
                                        label='uitvoering',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRCommunicatiekaart.uitvoering',
                                        definition='Type van communicatiekaart.',
                                        owner=self)

    @property
    def dnsNaam(self):
        """De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""
        return self._dnsNaam.get_waarde()

    @dnsNaam.setter
    def dnsNaam(self, value):
        self._dnsNaam.set_waarde(value, owner=self)

    @property
    def heeftSmartguard(self):
        """Smartguard aanwezig?"""
        return self._heeftSmartguard.get_waarde()

    @heeftSmartguard.setter
    def heeftSmartguard(self, value):
        self._heeftSmartguard.set_waarde(value, owner=self)

    @property
    def ipAdres(self):
        """IP-adres."""
        return self._ipAdres.get_waarde()

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def telefoonnummer(self):
        """Telefoonnummer."""
        return self._telefoonnummer.get_waarde()

    @telefoonnummer.setter
    def telefoonnummer(self, value):
        self._telefoonnummer.set_waarde(value, owner=self)

    @property
    def typeGeheugen(self):
        """Type opslaggeheugen op de aanwezige SD-kaart."""
        return self._typeGeheugen.get_waarde()

    @typeGeheugen.setter
    def typeGeheugen(self, value):
        self._typeGeheugen.set_waarde(value, owner=self)

    @property
    def uitvoering(self):
        """Type van communicatiekaart."""
        return self._uitvoering.get_waarde()

    @uitvoering.setter
    def uitvoering(self, value):
        self._uitvoering.set_waarde(value, owner=self)
