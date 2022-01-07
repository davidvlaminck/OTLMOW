# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRackMerk(Keuzelijst):
    """Merken voor racks."""

    def __init__(self):
        super().__init__(naam="KlRackMerk",
                         label="Rack merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRackMerk",
                         definition="Merken voor racks.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRackMerk")
