# coding=utf-8
from OTLModel.Classes.VRModuleMetFirmware import VRModuleMetFirmware
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVrStuurkaartCommunicatieprotocol import KlVrStuurkaartCommunicatieprotocol


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRStuurkaart(VRModuleMetFirmware):
    """Ook wel basissturing genoemd. Dit is de hoofdprocessorkaart van de VRI. Hier wordt het instructieprogramma en het kruispuntprogramma ingeladen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRStuurkaart"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.communicatieprotocol = KeuzelijstField(naam="communicatieprotocol",
                                                    label="communicatieprotocol",
                                                    lijst=KlVrStuurkaartCommunicatieprotocol(),
                                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRStuurkaart.communicatieprotocol",
                                                    definition="Gebruikte communicatieprotocol voor de stuurkaart.",
                                                    constraints="",
                                                    usagenote="",
                                                    deprecated_version="")
        """Gebruikte communicatieprotocol voor de stuurkaart."""
