# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAIDModuleType import KlAIDModuleType
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class AIDModule(AIMNaamObject):
    """Aparte hardware module voor automatische incidentdetectie op camerabeelden. De module kan centraal of lokaal opgesteld staan maar altijd als apart onderdeel, niet als deel van de camera die de beelden doorstuurt. Ze kan gebruikt worden voor modules die analoge beelden analyseren en voor modules die werken op basis van digitale beelden. Het doel is om op een automatische en zo intelligent mogelijk manier gebeurtenissen uit de beelden van een CCTV-camera te halen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AIDModule"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.configBestand = DtcDocument()
        """Configuratiebestand van de configuratie van de AID."""
        self.configBestand.naam = "configBestand"
        self.configBestand.label = "config bestand"
        self.configBestand.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AIDModule.configBestand"
        self.configBestand.definition = "Configuratiebestand van de configuratie van de AID."
        self.configBestand.constraints = ""
        self.configBestand.usagenote = ""
        self.configBestand.deprecated_version = ""

        self.dnsNaam = StringField(naam="dnsNaam",
                                   label="DNS naam",
                                   objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AIDModule.dnsNaam",
                                   definition="De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""

        self.ipAdres = DteIPv4Adres()
        """Het IP-adres van de AID-module."""
        self.ipAdres.naam = "ipAdres"
        self.ipAdres.label = "ip adres datastring"
        self.ipAdres.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AIDModule.ipAdres"
        self.ipAdres.definition = "Het IP-adres van de AID-module."
        self.ipAdres.constraints = ""
        self.ipAdres.usagenote = ""
        self.ipAdres.deprecated_version = ""

        self.technischeFiche = DtcDocument()
        """Technische fiche van de AID-module."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AIDModule.technischeFiche"
        self.technischeFiche.definition = "Technische fiche van de AID-module."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = "Bestanden van het type pdf."
        self.technischeFiche.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlAIDModuleType(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AIDModule.type",
                                    definition="Het type van de AID-module.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van de AID-module."""
