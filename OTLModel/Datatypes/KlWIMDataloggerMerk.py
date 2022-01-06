# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWIMDataloggerMerk(Keuzelijst):
    """Het merk van de WIM-datalogger."""

    def __init__(self):
        super().__init__(naam="KlWIMDataloggerMerk",
                         label="WIM-datalogger merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWIMDataloggerMerk",
                         definition="Het merk van de WIM-datalogger.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWIMDataloggerMerk")

