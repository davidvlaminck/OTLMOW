from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLComplexDatatypeCreator
class DtcAfmetingBxlxhInMm(ComplexField):
    """Complex datatype voor de afmeting van de breedte,de lengte en hoogte in millimeter."""

    def __init__(self):
        super().__init__(naam="DtcAfmetingBxlxhInMm",
                         label="Afmeting bxlxh in millimeter",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInMm",
                         definition="Complex datatype voor de afmeting van de breedte,de lengte en hoogte in millimeter.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.breedte = KwantWrdInMillimeter()
        self.waarde.breedte.naam = "breedte"
        self.waarde.breedte.label = "breedte"
        self.waarde.breedte.definition = "De breedte in millimeter."
        self.waarde.breedte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInMm.breedte"
        self.waarde.breedte.overerving = 0
        self.waarde.breedte.constraints = ""
        self.waarde.breedte.readonly = 0
        self.waarde.breedte.usagenote = ""
        self.waarde.breedte.deprecated_version = ""
        self.breedte = self.waarde.breedte
        """De breedte in millimeter."""

        self.waarde.hoogte = KwantWrdInMillimeter()
        self.waarde.hoogte.naam = "hoogte"
        self.waarde.hoogte.label = "hoogte"
        self.waarde.hoogte.definition = "De hoogte in millimeter."
        self.waarde.hoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInMm.hoogte"
        self.waarde.hoogte.overerving = 0
        self.waarde.hoogte.constraints = ""
        self.waarde.hoogte.readonly = 0
        self.waarde.hoogte.usagenote = ""
        self.waarde.hoogte.deprecated_version = ""
        self.hoogte = self.waarde.hoogte
        """De hoogte in millimeter."""

        self.waarde.lengte = KwantWrdInMillimeter()
        self.waarde.lengte.naam = "lengte"
        self.waarde.lengte.label = "lengte"
        self.waarde.lengte.definition = "De lengte in millimeter."
        self.waarde.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInMm.lengte"
        self.waarde.lengte.overerving = 0
        self.waarde.lengte.constraints = ""
        self.waarde.lengte.readonly = 0
        self.waarde.lengte.usagenote = ""
        self.waarde.lengte.deprecated_version = ""
        self.lengte = self.waarde.lengte
        """De lengte in millimeter."""
