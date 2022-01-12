# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPTRegelaarModuleMerk(Keuzelijst):
    """Keuzelijst met merknamen voor PTRegelaarModule."""

    def __init__(self):
        super().__init__(naam="KlPTRegelaarModuleMerk",
                         label="PT regelaarmodule merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlPTRegelaarModuleMerk",
                         definition="Keuzelijst met merknamen voor PTRegelaarModule.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPTRegelaarModuleMerk")

