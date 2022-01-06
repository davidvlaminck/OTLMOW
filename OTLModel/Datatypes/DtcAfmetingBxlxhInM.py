# coding=utf-8
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
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
        """De breedte in meter."""
        self.waarde.breedte.naam = "breedte"
        self.waarde.breedte.label = "breedte"
        self.waarde.breedte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInM.breedte"
        self.waarde.breedte.definition = "De breedte in meter."
        self.waarde.breedte.constraints = ""
        self.waarde.breedte.usagenote = ""
        self.waarde.breedte.deprecated_version = ""
        self.breedte = self.waarde.breedte

        self.waarde.hoogte = KwantWrdInMeter()
        """De hoogte in meter."""
        self.waarde.hoogte.naam = "hoogte"
        self.waarde.hoogte.label = "hoogte"
        self.waarde.hoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInM.hoogte"
        self.waarde.hoogte.definition = "De hoogte in meter."
        self.waarde.hoogte.constraints = ""
        self.waarde.hoogte.usagenote = ""
        self.waarde.hoogte.deprecated_version = ""
        self.hoogte = self.waarde.hoogte

        self.waarde.lengte = KwantWrdInMeter()
        """De lengte in meter."""
        self.waarde.lengte.naam = "lengte"
        self.waarde.lengte.label = "lengte"
        self.waarde.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInM.lengte"
        self.waarde.lengte.definition = "De lengte in meter."
        self.waarde.lengte.constraints = ""
        self.waarde.lengte.usagenote = ""
        self.waarde.lengte.deprecated_version = ""
        self.lengte = self.waarde.lengte
