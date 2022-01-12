# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPoEInjectorMerk(Keuzelijst):
    """Het merk van de PoE-injector."""

    def __init__(self):
        super().__init__(naam="KlPoEInjectorMerk",
                         label="Power over ethernet injector merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPoEInjectorMerk",
                         definition="Het merk van de PoE-injector.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPoEInjectorMerk")

