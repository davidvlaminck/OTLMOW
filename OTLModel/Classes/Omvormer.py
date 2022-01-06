from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlOmvormerMerk import KlOmvormerMerk
from OTLModel.Datatypes.KlOmvormerModelnaam import KlOmvormerModelnaam
from OTLModel.Datatypes.KlOmvormerType import KlOmvormerType
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Omvormer(AIMNaamObject):
    """Een object, bijna altijd geplaatst in paar geplaatst, omvorming en "de"-omvorming, dat een signaal binnenneemt en terug uitstuurt maar dan  op een andere manier. Er zijn een hele reeks manieren.

- Omvorming waar er gewijzigd wordt van type kabel om dezelfde boodschap over te versturen, bv. omvorming van UTP naar Coax.

- Omvorming van codering bv. analoog naar digitaal en in omgekeerde richting digitaal naar analoog (omvorming van codering analoog-digitaal verschilt van een encoder omdat een encoder een eindproduct aflevert; in dit geval is de omvorming ter ondersteuning het transport en zal er altijd een omvorming zijn terug naar analoog)

- Omvorming  die de gegevens opnieuw versterkt zodat ze over een langere afstand kunnen getransporteerd worden. Deze variant heeft niet noodzakelijk een tweede omvormer om terug te gaan naar het origineel."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.dnsNaam = StringField(naam="dnsNaam",
                                   label="DNS naam",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer.dnsNaam",
                                   definition="De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""

        self.ipAdres = DteIPv4Adres()
        """Het IP-adres van de omvormer."""
        self.ipAdres.naam = "ipAdres"
        self.ipAdres.label = "ip adres"
        self.ipAdres.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer.ipAdres"
        self.ipAdres.definition = "Het IP-adres van de omvormer."
        self.ipAdres.constraints = ""
        self.ipAdres.usagenote = ""
        self.ipAdres.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlOmvormerMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer.merk",
                                    definition="Het merk van de omvormer.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de omvormer."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlOmvormerModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer.modelnaam",
                                         definition="De modelnaam van de omvormer.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de omvormer."""

        self.technischeFiche = DtcDocument()
        """Technische fiche van de omvormer."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer.technischeFiche"
        self.technischeFiche.definition = "Technische fiche van de omvormer."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = "Bestanden van het type pdf."
        self.technischeFiche.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlOmvormerType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer.type",
                                    definition="De soort omvorming die gebeurt er in de omvormer.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De soort omvorming die gebeurt er in de omvormer."""
