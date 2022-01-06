# coding=utf-8
from OTLModel.Classes.Grasland import Grasland
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlNSB import KlNSB


# Generated with OTLClassCreator. To modify: extend, do not edit
class BloemrijkGraslandGraslandfase4(Grasland):
    """G4 - Fijn mozaïek van grassen, kruiden, russen en zeggen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BloemrijkGraslandGraslandfase4"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.huidigNatuurbeeld = KeuzelijstField(naam="huidigNatuurbeeld",
                                                 label="huidig natuurbeeld",
                                                 lijst=KlNSB(),
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BloemrijkGraslandGraslandfase4.huidigNatuurbeeld",
                                                 definition="Bepaling van het vegetatietype op basis van terreininventarisatie.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Bepaling van het vegetatietype op basis van terreininventarisatie."""
