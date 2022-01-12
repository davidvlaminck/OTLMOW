# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDrukknopMerk(Keuzelijst):
    """Keuzelijst met merknamen voor Drukknop."""

    def __init__(self):
        super().__init__(naam="KlDrukknopMerk",
                         label="Drukknop merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDrukknopMerk",
                         definition="Keuzelijst met merknamen voor Drukknop.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDrukknopMerk")

