from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLComplexDatatypeCreator
class DtcAfmetingBxlInCm(ComplexField):
    """Complex datatype voor de afmeting van de breedte en de lengte in centimeter."""

    def __init__(self):
        super().__init__(naam="DtcAfmetingBxlInCm",
                         label="Afmeting bxl in centimeter",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlInCm",
                         definition="Complex datatype voor de afmeting van de breedte en de lengte in centimeter.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.breedte = KwantWrdInCentimeter()
        """De breedte in centimeter."""
        self.waarde.breedte.naam = "breedte"
        self.waarde.breedte.label = "breedte"
        self.waarde.breedte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlInCm.breedte"
        self.waarde.breedte.definition = "De breedte in centimeter."
        self.waarde.breedte.constraints = ""
        self.waarde.breedte.usagenote = ""
        self.waarde.breedte.deprecated_version = ""
        self.breedte = self.waarde.breedte

        self.waarde.lengte = KwantWrdInCentimeter()
        """De lengte in centimeter."""
        self.waarde.lengte.naam = "lengte"
        self.waarde.lengte.label = "lengte"
        self.waarde.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlInCm.lengte"
        self.waarde.lengte.definition = "De lengte in centimeter."
        self.waarde.lengte.constraints = ""
        self.waarde.lengte.usagenote = ""
        self.waarde.lengte.deprecated_version = ""
        self.lengte = self.waarde.lengte
