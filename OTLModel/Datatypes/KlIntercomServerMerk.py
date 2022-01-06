# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIntercomServerMerk(Keuzelijst):
    """Het merk van de intercomserver."""

    def __init__(self):
        super().__init__(naam="KlIntercomServerMerk",
                         label="Intercomserver merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIntercomServerMerk",
                         definition="Het merk van de intercomserver.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIntercomServerMerk")

