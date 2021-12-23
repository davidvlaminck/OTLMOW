from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlMarkeringWaarborgperiode import KlMarkeringWaarborgperiode
from OTLModel.Datatypes.KlSignalisatieMarkeringOpvatting import KlSignalisatieMarkeringOpvatting


# Generated with OTLComplexDatatypeCreator
class DtcMarkeringOpvatting(ComplexField):
    """Complex datatype voor de opvatting van een markering."""

    def __init__(self):
        super().__init__(naam="DtcMarkeringOpvatting",
                         label="Markering opvatting",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcMarkeringOpvatting",
                         definition="Complex datatype voor de opvatting van een markering.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.opvatting = KeuzelijstField(naam="opvatting",
                                                label="opvatting",
                                                lijst=KlSignalisatieMarkeringOpvatting(),
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcMarkeringOpvatting.opvatting",
                                                definition="De opvatting van de markering, zijnde middelenverbintenis of resultaatsverbintenis.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        self.opvatting = self.waarde.opvatting
        """De opvatting van de markering, zijnde middelenverbintenis of resultaatsverbintenis."""

        self.waarde.waarborgperiode = KeuzelijstField(naam="waarborgperiode",
                                                      label="waarborgperiode",
                                                      lijst=KlMarkeringWaarborgperiode(),
                                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcMarkeringOpvatting.waarborgperiode",
                                                      definition="De periode waarin de markering moet voldoen aan de resultaatseisen.",
                                                      constraints="",
                                                      usagenote="",
                                                      deprecated_version="")
        self.waarborgperiode = self.waarde.waarborgperiode
        """De periode waarin de markering moet voldoen aan de resultaatseisen."""
