from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAudioversterkerMerk import KlAudioversterkerMerk
from OTLModel.Datatypes.KlAudioversterkerModelnaam import KlAudioversterkerModelnaam
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator
class Audioversterker(AIMNaamObject):
    """Elk toestel dat een inkomend audiosignaal omzet naar een signaal dat meerdere luidsprekers kan aansturen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Audioversterker"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.dnsNaam = StringField(naam="dnsNaam",
                                   label="DNS naam",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Audioversterker.dnsNaam",
                                   definition="De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""

        self.ipAdres = DteIPv4Adres()
        """Het IP-adres van de audioversterker."""
        self.ipAdres.naam = "ipAdres"
        self.ipAdres.label = "IP-adres"
        self.ipAdres.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Audioversterker.ipAdres"
        self.ipAdres.definition = "Het IP-adres van de audioversterker."
        self.ipAdres.constraints = ""
        self.ipAdres.usagenote = ""
        self.ipAdres.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlAudioversterkerMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Audioversterker.merk",
                                    definition="Het merk van de audioversterker.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de audioversterker."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlAudioversterkerModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Audioversterker.modelnaam",
                                         definition="De modelnaam van de audioversterker.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de audioversterker."""

        self.technischeFiche = DtcDocument()
        """De technische fiche van de audioversterker."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Audioversterker.technischeFiche"
        self.technischeFiche.definition = "De technische fiche van de audioversterker."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""
