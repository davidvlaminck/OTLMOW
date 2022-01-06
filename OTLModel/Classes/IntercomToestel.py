from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAudioTransportType import KlAudioTransportType
from OTLModel.Datatypes.KlIntercomMerk import KlIntercomMerk
from OTLModel.Datatypes.KlIntercomModelnaam import KlIntercomModelnaam
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class IntercomToestel(AIMNaamObject):
    """Het toestel dat deel uitmaakt van een intercomsysteem en audio- en/of videocommunicatie tussen twee personen mogelijk maakt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.dnsNaam = StringField(naam="dnsNaam",
                                   label="DNS naam",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.dnsNaam",
                                   definition="De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""

        self.heeftVideo = BooleanField(naam="heeftVideo",
                                       label="heeft video",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.heeftVideo",
                                       definition="Geeft aan of communicatie tussen personen al dan niet via video kan verlopen.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Geeft aan of communicatie tussen personen al dan niet via video kan verlopen."""

        self.ipAdres = DteIPv4Adres()
        """Het IP-adres van het intercomtoestel."""
        self.ipAdres.naam = "ipAdres"
        self.ipAdres.label = "IP-adres"
        self.ipAdres.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.ipAdres"
        self.ipAdres.definition = "Het IP-adres van het intercomtoestel."
        self.ipAdres.constraints = ""
        self.ipAdres.usagenote = ""
        self.ipAdres.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlIntercomMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.merk",
                                    definition="Het merk van het intercomtoestel.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van het intercomtoestel."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlIntercomModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.modelnaam",
                                         definition="De modelnaam van het intercomtoestel.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van het intercomtoestel."""

        self.technischeFiche = DtcDocument()
        """De technische fiche van het intercomtoestel."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.technischeFiche"
        self.technischeFiche.definition = "De technische fiche van het intercomtoestel."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""

        self.transportType = KeuzelijstField(naam="transportType",
                                             label="transporttype",
                                             lijst=KlAudioTransportType(),
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.transportType",
                                             definition="Geeft het type van (video- en) audiotransport aan van het intercomtoestel binnen het intercomsysteem.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Geeft het type van (video- en) audiotransport aan van het intercomtoestel binnen het intercomsysteem."""
