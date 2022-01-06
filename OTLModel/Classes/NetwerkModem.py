from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class NetwerkModem(AIMNaamObject):
    """Een netwerkmodem legt een netwerkverbinding via een vast of mobiel telecomnetwerk; dit wordt enkel gebruikt bij het ontbreken van een netwerkswitch."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NetwerkModem"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.dnsNaam = StringField(naam="dnsNaam",
                                   label="DNS naam",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NetwerkModem.dnsNaam",
                                   definition="De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""

        self.ipAdres = DteIPv4Adres()
        """IP-adres van de netwerkmodem."""
        self.ipAdres.naam = "ipAdres"
        self.ipAdres.label = "ip adres"
        self.ipAdres.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NetwerkModem.ipAdres"
        self.ipAdres.definition = "IP-adres van de netwerkmodem."
        self.ipAdres.constraints = ""
        self.ipAdres.usagenote = ""
        self.ipAdres.deprecated_version = ""
