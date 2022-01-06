# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPompMerk(Keuzelijst):
    """Lijst met merknamen voor pompen."""

    def __init__(self):
        super().__init__(naam="KlPompMerk",
                         label="Typepomp merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPompMerk",
                         definition="Lijst met merknamen voor pompen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPompMerk")

