# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFietstelsysteemModelnaam(Keuzelijst):
    """Lijst met mogelijke modelnamen voor fietstelsystemen."""

    def __init__(self):
        super().__init__(naam="KlFietstelsysteemModelnaam",
                         label="Modelnaam fietstelsysteem",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFietstelsysteemModelnaam",
                         definition="Lijst met mogelijke modelnamen voor fietstelsystemen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFietstelsysteemModelnaam")

