# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVRModuleMetFirmwareMerk(Keuzelijst):
    """Lijst met merken van VR-modules met firmware."""

    def __init__(self):
        super().__init__(naam="KlVRModuleMetFirmwareMerk",
                         label="VR-module met firmware merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVRModuleMetFirmwareMerk",
                         definition="Lijst met merken van VR-modules met firmware.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVRModuleMetFirmwareMerk")

