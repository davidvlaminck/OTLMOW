from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlANPRMerk import KlANPRMerk
from OTLModel.Datatypes.KlANPRModelnaam import KlANPRModelnaam
from OTLModel.Datatypes.KlAlgRijrichting import KlAlgRijrichting
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class ANPRCamera(AIMNaamObject):
    """Nummerplaatherkenningscamera: een camera die als output de nummerplaat van een voertuig in tekst geeft en een foto van het deel van het voertuig waar de nummerplaat zich bevindt. Afhankelijk van het merk en type gecombineerd met een al dan niet bewegend overzichtsbeeld."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.dnsNaam = StringField(naam="dnsNaam",
                                   label="DNS naam",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.dnsNaam",
                                   definition="De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""

        self.heeftFlits = BooleanField(naam="heeftFlits",
                                       label="heeft flits",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.heeftFlits",
                                       definition="Geeft aan of de camera een externe infrarood flits heeft.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Geeft aan of de camera een externe infrarood flits heeft."""

        self.ipAdres = DteIPv4Adres()
        """IP-adres van de ANPR-camera."""
        self.ipAdres.naam = "ipAdres"
        self.ipAdres.label = "ip adres"
        self.ipAdres.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.ipAdres"
        self.ipAdres.definition = "IP-adres van de ANPR-camera."
        self.ipAdres.constraints = ""
        self.ipAdres.usagenote = ""
        self.ipAdres.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlANPRMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.merk",
                                    definition="Het merk van de ANPR-camera.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de ANPR-camera."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlANPRModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.modelnaam",
                                         definition="De modelnaam van de ANPR-camera.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de ANPR-camera."""

        self.rijrichting = KeuzelijstField(naam="rijrichting",
                                           label="rijrichting",
                                           lijst=KlAlgRijrichting(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.rijrichting",
                                           definition="De rijrichting van de voertuigen die door de camera geregistreerd worden.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """De rijrichting van de voertuigen die door de camera geregistreerd worden."""

        self.technischeFiche = DtcDocument()
        """Technische fiche van dit element."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.technischeFiche"
        self.technischeFiche.definition = "Technische fiche van dit element."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = "Bestanden van het type pdf."
        self.technischeFiche.deprecated_version = ""
