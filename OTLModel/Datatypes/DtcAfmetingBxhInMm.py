# coding=utf-8
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxhInMm(ComplexField):
    """Complex datatype voor de afmeting van de breedte en hoogte in millimeter."""

    def __init__(self):
        super().__init__(naam="DtcAfmetingBxhInMm",
                         label="Afmeting bxh in millimeter",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxhInMm",
                         definition="Complex datatype voor de afmeting van de breedte en hoogte in millimeter.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.breedte = KwantWrdInMillimeter()
        """De breedte in millimeter."""
        self.waarde.breedte.naam = "breedte"
        self.waarde.breedte.label = "breedte"
        self.waarde.breedte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxhInMm.breedte"
        self.waarde.breedte.definition = "De breedte in millimeter."
        self.waarde.breedte.constraints = ""
        self.waarde.breedte.usagenote = ""
        self.waarde.breedte.deprecated_version = ""
        self.breedte = self.waarde.breedte

        self.waarde.hoogte = KwantWrdInMillimeter()
        """De hoogte in millimeter."""
        self.waarde.hoogte.naam = "hoogte"
        self.waarde.hoogte.label = "hoogte"
        self.waarde.hoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxhInMm.hoogte"
        self.waarde.hoogte.definition = "De hoogte in millimeter."
        self.waarde.hoogte.constraints = ""
        self.waarde.hoogte.usagenote = ""
        self.waarde.hoogte.deprecated_version = ""
        self.hoogte = self.waarde.hoogte
