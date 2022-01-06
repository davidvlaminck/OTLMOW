# coding=utf-8
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcKrimpvoeg(ComplexField):
    """Complex datatype voor de informatie van de krimpvoegen."""

    def __init__(self):
        super().__init__(naam="DtcKrimpvoeg",
                         label="Krimpvoeg",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcKrimpvoeg",
                         definition="Complex datatype voor de informatie van de krimpvoegen.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.krimpvoegFrequentie = KwantWrdInMeter()
        """De afstand tussen de krimpvoegen in meter."""
        self.waarde.krimpvoegFrequentie.naam = "krimpvoegFrequentie"
        self.waarde.krimpvoegFrequentie.label = "krimpvoeg frequentie"
        self.waarde.krimpvoegFrequentie.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcKrimpvoeg.krimpvoegFrequentie"
        self.waarde.krimpvoegFrequentie.definition = "De afstand tussen de krimpvoegen in meter."
        self.waarde.krimpvoegFrequentie.constraints = ""
        self.waarde.krimpvoegFrequentie.usagenote = ""
        self.waarde.krimpvoegFrequentie.deprecated_version = ""
        self.krimpvoegFrequentie = self.waarde.krimpvoegFrequentie

        self.waarde.totaleLengte = KwantWrdInMeter()
        """De totale lengte in meter."""
        self.waarde.totaleLengte.naam = "totaleLengte"
        self.waarde.totaleLengte.label = "lengte"
        self.waarde.totaleLengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcKrimpvoeg.totaleLengte"
        self.waarde.totaleLengte.definition = "De totale lengte in meter."
        self.waarde.totaleLengte.constraints = ""
        self.waarde.totaleLengte.usagenote = ""
        self.waarde.totaleLengte.deprecated_version = ""
        self.totaleLengte = self.waarde.totaleLengte
