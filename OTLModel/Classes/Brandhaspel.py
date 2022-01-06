from OTLModel.Classes.Brandvoorziening import Brandvoorziening
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBrandhaspelMerk import KlBrandhaspelMerk
from OTLModel.Datatypes.KlBrandhaspelModelnaam import KlBrandhaspelModelnaam
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLModel.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter
from OTLModel.Datatypes.KwantWrdInKubiekeMeterPerSeconde import KwantWrdInKubiekeMeterPerSeconde
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brandhaspel(Brandvoorziening):
    """Een brandslang met spuitmond,opgerold op een haspel."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandhaspel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.buitendiameter = KwantWrdInCentimeter()
        """Buitendiameter van de slang op de haspel."""
        self.buitendiameter.naam = "buitendiameter"
        self.buitendiameter.label = "buitendiameter"
        self.buitendiameter.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandhaspel.buitendiameter"
        self.buitendiameter.definition = "Buitendiameter van de slang op de haspel."
        self.buitendiameter.constraints = ""
        self.buitendiameter.usagenote = ""
        self.buitendiameter.deprecated_version = ""

        self.keuringsdatum = DateField(naam="keuringsdatum",
                                       label="keuringsdatum",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandhaspel.keuringsdatum",
                                       definition="Laatste datum waarop de haspel gekeurd is.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Laatste datum waarop de haspel gekeurd is."""

        self.maximaalVolumedebiet = KwantWrdInKubiekeMeterPerSeconde()
        """Het maximale debiet dat per tijdseenheid door de slang en spuitmond kan stromen."""
        self.maximaalVolumedebiet.naam = "maximaalVolumedebiet"
        self.maximaalVolumedebiet.label = "maximaal volumedebiet"
        self.maximaalVolumedebiet.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandhaspel.maximaalVolumedebiet"
        self.maximaalVolumedebiet.definition = "Het maximale debiet dat per tijdseenheid door de slang en spuitmond kan stromen."
        self.maximaalVolumedebiet.constraints = ""
        self.maximaalVolumedebiet.usagenote = ""
        self.maximaalVolumedebiet.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlBrandhaspelMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandhaspel.merk",
                                    definition="Het merk van de brandhaspel.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de brandhaspel."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlBrandhaspelModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandhaspel.modelnaam",
                                         definition="De modelnaam van de brandhaspel.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de brandhaspel."""

        self.slangLengte = KwantWrdInMeter()
        """Nuttige lengte van de brandslang op de haspel."""
        self.slangLengte.naam = "slangLengte"
        self.slangLengte.label = "slanglengte"
        self.slangLengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandhaspel.slangLengte"
        self.slangLengte.definition = "Nuttige lengte van de brandslang op de haspel."
        self.slangLengte.constraints = ""
        self.slangLengte.usagenote = ""
        self.slangLengte.deprecated_version = ""
