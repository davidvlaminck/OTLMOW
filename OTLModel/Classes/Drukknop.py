from OTLModel.Classes.NietWeggebondenDetectie import NietWeggebondenDetectie
from OTLModel.Datatypes.DtcTijdsduur import DtcTijdsduur
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDrukknopMerk import KlDrukknopMerk
from OTLModel.Datatypes.KlDrukknopModelnaam import KlDrukknopModelnaam
from OTLModel.Datatypes.KlDrukknopSoort import KlDrukknopSoort


# Generated with OTLClassCreator
class Drukknop(NietWeggebondenDetectie):
    """Drukknoppen zijn de toestellen die opgesteld zijn op kruispunten om de aanwezigheid te melden van voetgangers of fietsers die de rijweg wensen over te steken of voor het aanmelden van openbaar vervoer. De toestellen sturen een geheugenelement (module voor de sturing en visualisatie) in de verkeersregelaar aan, zodanig dat een kortstondig indrukken van de drukknop of kortstondig aanraken van de sensor volstaat opdat de aanvraag tot doorgang blijft gelden tot de doorgang verleend wordt"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukknop"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.bewakingstijd = DtcTijdsduur()
        """Wachttijd (in uren) waarna een alarm pas mag optreden."""
        self.bewakingstijd.naam = "bewakingstijd"
        self.bewakingstijd.label = "bewakingstijd"
        self.bewakingstijd.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukknop.bewakingstijd"
        self.bewakingstijd.definition = "Wachttijd (in uren) waarna een alarm pas mag optreden."
        self.bewakingstijd.constraints = ""
        self.bewakingstijd.usagenote = ""
        self.bewakingstijd.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlDrukknopMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukknop.merk",
                                    definition="De naam van het merk van de drukknop.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De naam van het merk van de drukknop."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlDrukknopModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukknop.modelnaam",
                                         definition="De modelnaam van de drukknop.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de drukknop."""

        self.soortDrukknop = KeuzelijstField(naam="soortDrukknop",
                                             label="soort drukknop",
                                             lijst=KlDrukknopSoort(),
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukknop.soortDrukknop",
                                             definition="Doelgroep van de drukknop (voetganger, fietser, ruiter,...).",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Doelgroep van de drukknop (voetganger, fietser, ruiter,...)."""
