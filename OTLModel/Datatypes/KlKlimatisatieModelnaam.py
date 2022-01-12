# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKlimatisatieModelnaam(Keuzelijst):
    """Modelnamen voor klimatisatiesystemen."""

    def __init__(self):
        super().__init__(naam="KlKlimatisatieModelnaam",
                         label="Klimatisatie modelnaam",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKlimatisatieModelnaam",
                         definition="Modelnamen voor klimatisatiesystemen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKlimatisatieModelnaam")

