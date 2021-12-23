from OTLModel.Classes.VRModuleZFirmware import VRModuleZFirmware
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVRBatterijCUMerk import KlVRBatterijCUMerk
from OTLModel.Datatypes.KlVRBatterijCUModelnaam import KlVRBatterijCUModelnaam


# Generated with OTLClassCreator
class VRBatterijICU(VRModuleZFirmware):
    """Batterij die zorgt dat de primaire melding "spanning afwezig", in het geval van een spanningsuitval, nog kan doorgestuurd worden naar het afstandsbewakingssysteem."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBatterijICU"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlVRBatterijCUMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBatterijICU.merk",
                                    definition="De merknaam van de VR-batterij ICU.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De merknaam van de VR-batterij ICU."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlVRBatterijCUModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBatterijICU.modelnaam",
                                         definition="De modelnaam van de VR-batterij ICU.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de VR-batterij ICU."""
