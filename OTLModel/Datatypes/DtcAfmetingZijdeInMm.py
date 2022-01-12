# coding=utf-8
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingZijdeInMm(ComplexField):
    """Complex datatype voor de afmeting van een zijde in millimeter."""

    def __init__(self):
        super().__init__(naam="DtcAfmetingZijdeInMm",
                         label="Afmeting zijde in millimeter",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingZijdeInMm",
                         definition="Complex datatype voor de afmeting van een zijde in millimeter.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.zijde = KwantWrdInMillimeter()
        """De afmeting van een zijde in millimeter."""
        self.waarde.zijde.naam = "zijde"
        self.waarde.zijde.label = "zijde"
        self.waarde.zijde.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingZijdeInMm.zijde"
        self.waarde.zijde.definition = "De afmeting van een zijde in millimeter."
        self.waarde.zijde.constraints = ""
        self.waarde.zijde.usagenote = ""
        self.waarde.zijde.deprecated_version = ""
        self.zijde = self.waarde.zijde
