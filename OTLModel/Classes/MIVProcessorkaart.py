# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class MIVProcessorkaart(AIMNaamObject):
    """Meten in Vlaanderen : processorkaart van de lokale verwerkingseenheid."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVProcessorkaart"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.dnsNaam = StringField(naam="dnsNaam",
                                   label="DNS naam",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVProcessorkaart.dnsNaam",
                                   definition="De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""

        self.ipAdres = DteIPv4Adres()
        """IP-adres van de MIV-processorkaart."""
        self.ipAdres.naam = "ipAdres"
        self.ipAdres.label = "ip adres"
        self.ipAdres.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVProcessorkaart.ipAdres"
        self.ipAdres.definition = "IP-adres van de MIV-processorkaart."
        self.ipAdres.constraints = ""
        self.ipAdres.usagenote = ""
        self.ipAdres.deprecated_version = ""

        self.softwareversie = StringField(naam="softwareversie",
                                          label="softwareversie",
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVProcessorkaart.softwareversie",
                                          definition="De opsomming van de verschillende software-patches.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """De opsomming van de verschillende software-patches."""
