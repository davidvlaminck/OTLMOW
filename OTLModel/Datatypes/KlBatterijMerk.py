# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBatterijMerk(Keuzelijst):
    """Het merk van de batterij."""

    def __init__(self):
        super().__init__(naam="KlBatterijMerk",
                         label="Batterij merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBatterijMerk",
                         definition="Het merk van de batterij.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBatterijMerk")

