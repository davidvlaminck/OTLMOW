# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSeinlantaarnMerk(Keuzelijst):
    """Keuzelijst met merknamen voor Seinlantaarn."""

    def __init__(self):
        super().__init__(naam="KlSeinlantaarnMerk",
                         label="seinlantaarn merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlSeinlantaarnMerk",
                         definition="Keuzelijst met merknamen voor Seinlantaarn.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSeinlantaarnMerk")

