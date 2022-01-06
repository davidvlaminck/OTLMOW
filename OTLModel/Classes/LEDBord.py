# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Classes.Verkeersbord import Verkeersbord
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class LEDBord(AIMNaamObject, Verkeersbord):
    """Abstracte klasse die de gemeenschappelijke eigenschappen van verschillende types dynamische verkeersborden groepeert."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMNaamObject.__init__(self)
        Verkeersbord.__init__(self)

        self.aantalLichtsensoren = IntegerField(naam="aantalLichtsensoren",
                                                label="aantal lichtsensoren",
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.aantalLichtsensoren",
                                                definition="Het aantal lichtsensoren waar het bord over beschikt die continu de intensiteit van het invallend licht meten.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Het aantal lichtsensoren waar het bord over beschikt die continu de intensiteit van het invallend licht meten."""

        self.dnsNaam = StringField(naam="dnsNaam",
                                   label="DNS naam",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.dnsNaam",
                                   definition="De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""

        self.heeftDeurcontact = BooleanField(naam="heeftDeurcontact",
                                             label="heeft deurcontact",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.heeftDeurcontact",
                                             definition="Het LEDBord is beveiligd met een deurcontact dat waarschuwt voor ongeoorloofd openen van het bord door middel van een software-matig alarm.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Het LEDBord is beveiligd met een deurcontact dat waarschuwt voor ongeoorloofd openen van het bord door middel van een software-matig alarm."""

        self.ipAdres = DteIPv4Adres()
        """Het IP netwerkadres van het LEDBord."""
        self.ipAdres.naam = "ipAdres"
        self.ipAdres.label = "ip adres"
        self.ipAdres.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.ipAdres"
        self.ipAdres.definition = "Het IP netwerkadres van het LEDBord."
        self.ipAdres.constraints = ""
        self.ipAdres.usagenote = ""
        self.ipAdres.deprecated_version = ""

        self.logischeGroepVerkeerscentrum = StringField(naam="logischeGroepVerkeerscentrum",
                                                        label="logische groep verkeerscentrum",
                                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.logischeGroepVerkeerscentrum",
                                                        definition="Identificator van de logische groep toegekend door het Verkeerscentrum.",
                                                        constraints="",
                                                        usagenote="",
                                                        deprecated_version="")
        """Identificator van de logische groep toegekend door het Verkeerscentrum."""

        self.protocol = StringField(naam="protocol",
                                    label="protocol",
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.protocol",
                                    definition="Communicatieprotocol waarmee het LEDBord wordt aangestuurd.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Communicatieprotocol waarmee het LEDBord wordt aangestuurd."""

        self.technischeFiche = DtcDocument()
        """Document met technische informatie over het LEDBord."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.technischeFiche"
        self.technischeFiche.definition = "Document met technische informatie over het LEDBord."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""

        self.versie = StringField(naam="versie",
                                  label="versie",
                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.versie",
                                  definition="Versie van het LEDBord.",
                                  constraints="",
                                  usagenote="",
                                  deprecated_version="")
        """Versie van het LEDBord."""
