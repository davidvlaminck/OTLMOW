from abc import abstractmethod
from OTLModel.Classes.VerkeersregelaarModule import VerkeersregelaarModule
from OTLModel.Classes.FirmwareObject import FirmwareObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVRModuleMetFirmwareMerk import KlVRModuleMetFirmwareMerk
from OTLModel.Datatypes.KlVRModuleMetFirmwareModelnaam import KlVRModuleMetFirmwareModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRModuleMetFirmware(VerkeersregelaarModule, FirmwareObject):
    """Abstracte voor modules met firmware van een verkeersregelaar."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRModuleMetFirmware"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        VerkeersregelaarModule.__init__(self)
        FirmwareObject.__init__(self)

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlVRModuleMetFirmwareMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRModuleMetFirmware.merk",
                                    definition="Het merk van de VR module met Firmware.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de VR module met Firmware."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlVRModuleMetFirmwareModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRModuleMetFirmware.modelnaam",
                                         definition="De modelnaam/product range van de VR module met Firmware.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam/product range van de VR module met Firmware."""
