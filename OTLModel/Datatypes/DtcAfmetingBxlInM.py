# coding=utf-8
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxlInM(ComplexField):
    """Complex datatype voor de afmeting van de breedte en de lengte in meter."""

    def __init__(self):
        super().__init__(naam="DtcAfmetingBxlInM",
                         label="Afmeting bxl in meter",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlInM",
                         definition="Complex datatype voor de afmeting van de breedte en de lengte in meter.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.breedte = KwantWrdInMeter()
        """De breedte in meter."""
        self.waarde.breedte.naam = "breedte"
        self.waarde.breedte.label = "breedte"
        self.waarde.breedte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlInM.breedte"
        self.waarde.breedte.definition = "De breedte in meter."
        self.waarde.breedte.constraints = ""
        self.waarde.breedte.usagenote = ""
        self.waarde.breedte.deprecated_version = ""
        self.breedte = self.waarde.breedte

        self.waarde.lengte = KwantWrdInMeter()
        """De lengte in meter."""
        self.waarde.lengte.naam = "lengte"
        self.waarde.lengte.label = "lengte"
        self.waarde.lengte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlInM.lengte"
        self.waarde.lengte.definition = "De lengte in meter."
        self.waarde.lengte.constraints = ""
        self.waarde.lengte.usagenote = ""
        self.waarde.lengte.deprecated_version = ""
        self.lengte = self.waarde.lengte
