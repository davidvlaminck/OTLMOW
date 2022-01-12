# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCabineMerk(Keuzelijst):
    """Merknamen voor cabines."""

    def __init__(self):
        super().__init__(naam="KlCabineMerk",
                         label="Cabine merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCabineMerk",
                         definition="Merknamen voor cabines.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCabineMerk")

