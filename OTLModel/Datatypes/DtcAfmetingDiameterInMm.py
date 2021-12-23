from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLComplexDatatypeCreator
class DtcAfmetingDiameterInMm(ComplexField):
    """Complex datatype voor de afmeting van een diameter in millimeter."""

    def __init__(self):
        super().__init__(naam="DtcAfmetingDiameterInMm",
                         label="Afmeting diameter in millimeter",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingDiameterInMm",
                         definition="Complex datatype voor de afmeting van een diameter in millimeter.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.diameter = KwantWrdInMillimeter()
        """De diameter in millimeter."""
        self.waarde.diameter.naam = "diameter"
        self.waarde.diameter.label = "diameter"
        self.waarde.diameter.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingDiameterInMm.diameter"
        self.waarde.diameter.definition = "De diameter in millimeter."
        self.waarde.diameter.constraints = ""
        self.waarde.diameter.usagenote = ""
        self.waarde.diameter.deprecated_version = ""
        self.diameter = self.waarde.diameter
