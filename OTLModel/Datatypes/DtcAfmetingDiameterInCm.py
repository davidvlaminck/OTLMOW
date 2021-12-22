from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLComplexDatatypeCreator
class DtcAfmetingDiameterInCm(ComplexField):
    """Complex datatype voor de afmeting van een diameter in centimeter."""

    def __init__(self):
        super().__init__(naam="DtcAfmetingDiameterInCm",
                         label="Afmeting diameter in centimeter",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingDiameterInCm",
                         definition="Complex datatype voor de afmeting van een diameter in centimeter.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.diameter = KwantWrdInCentimeter()
        self.waarde.diameter.naam = "diameter"
        self.waarde.diameter.label = "diameter"
        self.waarde.diameter.definition = "De diameter in centimeter."
        self.waarde.diameter.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingDiameterInCm.diameter"
        self.waarde.diameter.overerving = 0
        self.waarde.diameter.constraints = ""
        self.waarde.diameter.readonly = 0
        self.waarde.diameter.usagenote = ""
        self.waarde.diameter.deprecated_version = ""
        self.diameter = self.waarde.diameter
        """De diameter in centimeter."""
