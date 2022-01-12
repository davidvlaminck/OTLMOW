# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZonnepaneelMerk(Keuzelijst):
    """Het merk van het zonnepaneel."""

    def __init__(self):
        super().__init__(naam="KlZonnepaneelMerk",
                         label="Zonnepaneel merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZonnepaneelMerk",
                         definition="Het merk van het zonnepaneel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZonnepaneelMerk")

