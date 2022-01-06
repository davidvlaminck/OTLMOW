# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVRModuleMetFirmwareModelnaam(Keuzelijst):
    """Lijst met modelnamen voor VR-modules met firmware."""

    def __init__(self):
        super().__init__(naam="KlVRModuleMetFirmwareModelnaam",
                         label="VR-module met firmware modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVRModuleMetFirmwareModelnaam",
                         definition="Lijst met modelnamen voor VR-modules met firmware.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVRModuleMetFirmwareModelnaam")

