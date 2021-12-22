from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLComplexDatatypeCreator
class DtcAfmetingBxlxhInM(ComplexField):
    """Complex datatype voor de afmeting van de breedte, de lengte en hoogte in meter."""

    def __init__(self):
        super().__init__(naam="DtcAfmetingBxlxhInM",
                         label="Afmeting bxlxh in meter",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInM",
                         definition="Complex datatype voor de afmeting van de breedte, de lengte en hoogte in meter.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.breedte = KwantWrdInMeter()
        self.waarde.breedte.naam = "breedte"
        self.waarde.breedte.label = "breedte"
        self.waarde.breedte.definition = "De breedte in meter."
        self.waarde.breedte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInM.breedte"
        self.waarde.breedte.overerving = 0
        self.waarde.breedte.constraints = ""
        self.waarde.breedte.readonly = 0
        self.waarde.breedte.usagenote = ""
        self.waarde.breedte.deprecated_version = ""
        self.breedte = self.waarde.breedte
        """De breedte in meter."""

        self.waarde.hoogte = KwantWrdInMeter()
        self.waarde.hoogte.naam = "hoogte"
        self.waarde.hoogte.label = "hoogte"
        self.waarde.hoogte.definition = "De hoogte in meter."
        self.waarde.hoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInM.hoogte"
        self.waarde.hoogte.overerving = 0
        self.waarde.hoogte.constraints = ""
        self.waarde.hoogte.readonly = 0
        self.waarde.hoogte.usagenote = ""
        self.waarde.hoogte.deprecated_version = ""
        self.hoogte = self.waarde.hoogte
        """De hoogte in meter."""

        self.waarde.lengte = KwantWrdInMeter()
        self.waarde.lengte.naam = "lengte"
        self.waarde.lengte.label = "lengte"
        self.waarde.lengte.definition = "De lengte in meter."
        self.waarde.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInM.lengte"
        self.waarde.lengte.overerving = 0
        self.waarde.lengte.constraints = ""
        self.waarde.lengte.readonly = 0
        self.waarde.lengte.usagenote = ""
        self.waarde.lengte.deprecated_version = ""
        self.lengte = self.waarde.lengte
        """De lengte in meter."""
