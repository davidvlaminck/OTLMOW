# coding=utf-8
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxlxhInCm(ComplexField):
    """Complex datatype voor de afmeting van de breedte,de lengte en hoogte in centimeter."""

    def __init__(self):
        super().__init__(naam="DtcAfmetingBxlxhInCm",
                         label="Afmeting bxlxh in centimeter",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInCm",
                         definition="Complex datatype voor de afmeting van de breedte,de lengte en hoogte in centimeter.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.breedte = KwantWrdInCentimeter()
        """De breedte in centimeter."""
        self.waarde.breedte.naam = "breedte"
        self.waarde.breedte.label = "breedte"
        self.waarde.breedte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInCm.breedte"
        self.waarde.breedte.definition = "De breedte in centimeter."
        self.waarde.breedte.constraints = ""
        self.waarde.breedte.usagenote = ""
        self.waarde.breedte.deprecated_version = ""
        self.breedte = self.waarde.breedte

        self.waarde.hoogte = KwantWrdInCentimeter()
        """De hoogte in centimeter."""
        self.waarde.hoogte.naam = "hoogte"
        self.waarde.hoogte.label = "hoogte"
        self.waarde.hoogte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInCm.hoogte"
        self.waarde.hoogte.definition = "De hoogte in centimeter."
        self.waarde.hoogte.constraints = ""
        self.waarde.hoogte.usagenote = ""
        self.waarde.hoogte.deprecated_version = ""
        self.hoogte = self.waarde.hoogte

        self.waarde.lengte = KwantWrdInCentimeter()
        """De lengte in centimeter."""
        self.waarde.lengte.naam = "lengte"
        self.waarde.lengte.label = "lengte"
        self.waarde.lengte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInCm.lengte"
        self.waarde.lengte.definition = "De lengte in centimeter."
        self.waarde.lengte.constraints = ""
        self.waarde.lengte.usagenote = ""
        self.waarde.lengte.deprecated_version = ""
        self.lengte = self.waarde.lengte
