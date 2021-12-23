from abc import abstractmethod
from OTLModel.Classes.Behuizing import Behuizing
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAlgMateriaal import KlAlgMateriaal


# Generated with OTLClassCreator
class Kast(Behuizing):
    """Abstracte voor allerlei types kasten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
        self.afmeting = DtcAfmetingBxlxhInMm()
        """Buitenafmeting van de kast als maximale breedte, lengte en hoogte in millimeter."""
        self.afmeting.naam = "afmeting"
        self.afmeting.label = "afmeting"
        self.afmeting.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast.afmeting"
        self.afmeting.definition = "Buitenafmeting van de kast als maximale breedte, lengte en hoogte in millimeter."
        self.afmeting.constraints = ""
        self.afmeting.usagenote = ""
        self.afmeting.deprecated_version = ""

        self.heeftVerlichting = BooleanField(naam="heeftVerlichting",
                                             label="heeft verlichting",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast.heeftVerlichting",
                                             definition="Geeft aan of er verlichting aanwezig is binnen de kast.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Geeft aan of er verlichting aanwezig is binnen de kast."""

        self.indelingsplan = DtcDocument()
        """Schematisch overzicht van de indeling van de kast volgens de aanwezige technieken in vooraanzicht."""
        self.indelingsplan.naam = "indelingsplan"
        self.indelingsplan.label = "indelingsplan"
        self.indelingsplan.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast.indelingsplan"
        self.indelingsplan.definition = "Schematisch overzicht van de indeling van de kast volgens de aanwezige technieken in vooraanzicht."
        self.indelingsplan.constraints = ""
        self.indelingsplan.usagenote = ""
        self.indelingsplan.deprecated_version = ""

        self.kastmateriaal = KeuzelijstField(naam="kastmateriaal",
                                             label="kastmateriaal",
                                             lijst=KlAlgMateriaal(),
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast.kastmateriaal",
                                             definition="Materiaal waaruit de kast is opgebouwd.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Materiaal waaruit de kast is opgebouwd."""
