# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVRBAZMerk(Keuzelijst):
    """Keuzelijst met merknamen voor VRBAZ."""

    def __init__(self):
        super().__init__(naam="KlVRBAZMerk",
                         label="VR-BAZ merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVRBAZMerk",
                         definition="Keuzelijst met merknamen voor VRBAZ.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVRBAZMerk")

