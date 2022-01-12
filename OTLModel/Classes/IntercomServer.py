# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAudioTransportType import KlAudioTransportType
from OTLModel.Datatypes.KlIntercomServerMerk import KlIntercomServerMerk
from OTLModel.Datatypes.KlIntercomServerModelnaam import KlIntercomServerModelnaam
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class IntercomServer(AIMNaamObject):
    """Centrale module - inclusief configuratiesoftware - die de intercomtoestellen koppelt, bv. per tunnel of per complex, en een gateway opzet naar de centrale systemen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.dnsNaam = StringField(naam="dnsNaam",
                                   label="DNS naam",
                                   objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer.dnsNaam",
                                   definition="De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""

        self.ipAdres = DteIPv4Adres()
        """Het IP-adres van de intercomserver."""
        self.ipAdres.naam = "ipAdres"
        self.ipAdres.label = "IP-adres"
        self.ipAdres.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer.ipAdres"
        self.ipAdres.definition = "Het IP-adres van de intercomserver."
        self.ipAdres.constraints = ""
        self.ipAdres.usagenote = ""
        self.ipAdres.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlIntercomServerMerk(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer.merk",
                                    definition="Het merk van de intercomserver.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de intercomserver."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlIntercomServerModelnaam(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer.modelnaam",
                                         definition="De modelnaam van de intercomserver.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de intercomserver."""

        self.technischeFiche = DtcDocument()
        """De technische fiche van de intercomserver."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer.technischeFiche"
        self.technischeFiche.definition = "De technische fiche van de intercomserver."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""

        self.transportType = KeuzelijstField(naam="transportType",
                                             label="transport type",
                                             lijst=KlAudioTransportType(),
                                             objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer.transportType",
                                             definition="Geeft aan op welke manier het audiosignaal wordt getransporteerd door het toestel.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Geeft aan op welke manier het audiosignaal wordt getransporteerd door het toestel."""
