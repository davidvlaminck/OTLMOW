from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlIpPowerSwitchType import KlIpPowerSwitchType
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class IpPowerSwitch(AIMNaamObject):
    """Een IP powerswitch levert netspanning (230V) aan achterliggende apparaten. Door in te loggen op de powerswitch kunt u de poort en dus de netspanning naar het aangesloten apparaat vanop afstand uit en aan zetten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IpPowerSwitch"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.dnsNaam = StringField(naam="dnsNaam",
                                   label="DNS naam",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IpPowerSwitch.dnsNaam",
                                   definition="De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""

        self.handleiding = DtcDocument()
        """De handleiding van de IP powerswitch."""
        self.handleiding.naam = "handleiding"
        self.handleiding.label = "handleiding"
        self.handleiding.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IpPowerSwitch.handleiding"
        self.handleiding.definition = "De handleiding van de IP powerswitch."
        self.handleiding.constraints = ""
        self.handleiding.usagenote = "Bestanden van het type pdf."
        self.handleiding.deprecated_version = ""

        self.ipAdres = DteIPv4Adres()
        """Het IP-adres van de IP power switch."""
        self.ipAdres.naam = "ipAdres"
        self.ipAdres.label = "ip adres"
        self.ipAdres.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IpPowerSwitch.ipAdres"
        self.ipAdres.definition = "Het IP-adres van de IP power switch."
        self.ipAdres.constraints = ""
        self.ipAdres.usagenote = ""
        self.ipAdres.deprecated_version = ""

        self.technischeFiche = DtcDocument()
        """De technische fiche  van de IP powerswitch."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IpPowerSwitch.technischeFiche"
        self.technischeFiche.definition = "De technische fiche  van de IP powerswitch."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = "Bestanden van het type pdf."
        self.technischeFiche.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlIpPowerSwitchType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IpPowerSwitch.type",
                                    definition="Merk en type van de IP powerswitch.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merk en type van de IP powerswitch."""
