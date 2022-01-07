# coding=utf-8
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlProfielhoogtemaat import KlProfielhoogtemaat
from OTLModel.Datatypes.KlProfielsoort import KlProfielsoort


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcProfieltype(ComplexField):
    """Complex datatype om de hoogtemaat en de soort van het profiel in te geven."""

    def __init__(self):
        super().__init__(naam="DtcProfieltype",
                         label="Profieltype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfieltype",
                         definition="Complex datatype om de hoogtemaat en de soort van het profiel in te geven.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.profielhoogtemaat = KeuzelijstField(naam="profielhoogtemaat",
                                                        label="profielhoogtemaat",
                                                        lijst=KlProfielhoogtemaat(),
                                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfieltype.profielhoogtemaat",
                                                        definition="Voorgedefinieerde hoogtemaat van een profiel.",
                                                        constraints="",
                                                        usagenote="",
                                                        deprecated_version="")
        self.profielhoogtemaat = self.waarde.profielhoogtemaat
        """Voorgedefinieerde hoogtemaat van een profiel."""

        self.waarde.profielsoort = KeuzelijstField(naam="profielsoort",
                                                   label="profielsoort",
                                                   lijst=KlProfielsoort(),
                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfieltype.profielsoort",
                                                   definition="Het type profiel (de meest genormeerde types).",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        self.profielsoort = self.waarde.profielsoort
        """Het type profiel (de meest genormeerde types)."""