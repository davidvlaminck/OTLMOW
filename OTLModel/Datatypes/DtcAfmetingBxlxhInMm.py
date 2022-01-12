# coding=utf-8
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxlxhInMm(ComplexField):
    """Complex datatype voor de afmeting van de breedte,de lengte en hoogte in millimeter."""

    def __init__(self):
        super().__init__(naam="DtcAfmetingBxlxhInMm",
                         label="Afmeting bxlxh in millimeter",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInMm",
                         definition="Complex datatype voor de afmeting van de breedte,de lengte en hoogte in millimeter.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.breedte = KwantWrdInMillimeter()
        """De breedte in millimeter."""
        self.waarde.breedte.naam = "breedte"
        self.waarde.breedte.label = "breedte"
        self.waarde.breedte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInMm.breedte"
        self.waarde.breedte.definition = "De breedte in millimeter."
        self.waarde.breedte.constraints = ""
        self.waarde.breedte.usagenote = ""
        self.waarde.breedte.deprecated_version = ""
        self.breedte = self.waarde.breedte

        self.waarde.hoogte = KwantWrdInMillimeter()
        """De hoogte in millimeter."""
        self.waarde.hoogte.naam = "hoogte"
        self.waarde.hoogte.label = "hoogte"
        self.waarde.hoogte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInMm.hoogte"
        self.waarde.hoogte.definition = "De hoogte in millimeter."
        self.waarde.hoogte.constraints = ""
        self.waarde.hoogte.usagenote = ""
        self.waarde.hoogte.deprecated_version = ""
        self.hoogte = self.waarde.hoogte

        self.waarde.lengte = KwantWrdInMillimeter()
        """De lengte in millimeter."""
        self.waarde.lengte.naam = "lengte"
        self.waarde.lengte.label = "lengte"
        self.waarde.lengte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInMm.lengte"
        self.waarde.lengte.definition = "De lengte in millimeter."
        self.waarde.lengte.constraints = ""
        self.waarde.lengte.usagenote = ""
        self.waarde.lengte.deprecated_version = ""
        self.lengte = self.waarde.lengte
