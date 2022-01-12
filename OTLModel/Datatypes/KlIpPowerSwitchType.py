# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIpPowerSwitchType(Keuzelijst):
    """Type van de IP powerswitch."""

    def __init__(self):
        super().__init__(naam="KlIpPowerSwitchType",
                         label="IP powerswitch type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIpPowerSwitchType",
                         definition="Type van de IP powerswitch.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIpPowerSwitchType")

