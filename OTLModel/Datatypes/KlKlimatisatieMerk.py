# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKlimatisatieMerk(Keuzelijst):
    """Merknamen voor klimatisatiesystemen."""

    def __init__(self):
        super().__init__(naam="KlKlimatisatieMerk",
                         label="Klimatisatie merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKlimatisatieMerk",
                         definition="Merknamen voor klimatisatiesystemen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKlimatisatieMerk")

