# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeerslichtMerk(Keuzelijst):
    """Keuzelijst met merknamen voor Verkeerslicht."""

    def __init__(self):
        super().__init__(naam="KlVerkeerslichtMerk",
                         label="verkeerslicht merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerkeerslichtMerk",
                         definition="Keuzelijst met merknamen voor Verkeerslicht.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeerslichtMerk")

