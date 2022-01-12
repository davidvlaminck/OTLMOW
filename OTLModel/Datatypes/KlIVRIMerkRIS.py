# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIMerkRIS(Keuzelijst):
    """Het merk van de RIS."""

    def __init__(self):
        super().__init__(naam="KlIVRIMerkRIS",
                         label="iVRIMerkRIS",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIMerkRIS",
                         definition="Het merk van de RIS.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIMerkRIS")

