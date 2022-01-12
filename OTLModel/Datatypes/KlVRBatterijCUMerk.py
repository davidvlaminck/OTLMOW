# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVRBatterijCUMerk(Keuzelijst):
    """Keuzelijst met merknamen voor VRBatterijCU."""

    def __init__(self):
        super().__init__(naam="KlVRBatterijCUMerk",
                         label="Batterij CU merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVRBatterijCUMerk",
                         definition="Keuzelijst met merknamen voor VRBatterijCU.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVRBatterijCUMerk")

