from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInMinuut import KwantWrdInMinuut
from OTLModel.Datatypes.KwantWrdInSeconde import KwantWrdInSeconde
from OTLModel.Datatypes.KwantWrdInUur import KwantWrdInUur


# Generated with OTLComplexDatatypeCreator
class DtcTijdsduur(ComplexField):
    """Complex datatype voor de instelling van een tijdsbepaling."""

    def __init__(self):
        super().__init__(naam="DtcTijdsduur",
                         label="Tijdsduur",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTijdsduur",
                         definition="Complex datatype voor de instelling van een tijdsbepaling.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.minuten = KwantWrdInMinuut()
        self.waarde.minuten.naam = "minuten"
        self.waarde.minuten.label = "minuten"
        self.waarde.minuten.definition = "Het aantal minuten."
        self.waarde.minuten.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTijdsduur.minuten"
        self.waarde.minuten.overerving = 0
        self.waarde.minuten.constraints = ""
        self.waarde.minuten.readonly = 0
        self.waarde.minuten.usagenote = ""
        self.waarde.minuten.deprecated_version = ""
        self.minuten = self.waarde.minuten
        """Het aantal minuten."""

        self.waarde.seconden = KwantWrdInSeconde()
        self.waarde.seconden.naam = "seconden"
        self.waarde.seconden.label = "seconden"
        self.waarde.seconden.definition = "Het aantal seconden."
        self.waarde.seconden.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTijdsduur.seconden"
        self.waarde.seconden.overerving = 0
        self.waarde.seconden.constraints = ""
        self.waarde.seconden.readonly = 0
        self.waarde.seconden.usagenote = ""
        self.waarde.seconden.deprecated_version = ""
        self.seconden = self.waarde.seconden
        """Het aantal seconden."""

        self.waarde.uren = KwantWrdInUur()
        self.waarde.uren.naam = "uren"
        self.waarde.uren.label = "uren"
        self.waarde.uren.definition = "Het aantal uren."
        self.waarde.uren.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTijdsduur.uren"
        self.waarde.uren.overerving = 0
        self.waarde.uren.constraints = ""
        self.waarde.uren.readonly = 0
        self.waarde.uren.usagenote = ""
        self.waarde.uren.deprecated_version = ""
        self.uren = self.waarde.uren
        """Het aantal uren."""
