from OTLModel.Classes.Grasland import Grasland
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlNSB import KlNSB


# Generated with OTLClassCreator
class SoortenrijkSchraalGraslandGraslandfase5(Grasland):
    """G5 - Een fijn, soortenrijk mozaïek van geel-, grijs- en blauwgroene laagblijvende schijngrassen (zeggen en russen) en kruiden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SoortenrijkSchraalGraslandGraslandfase5"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.huidigNatuurbeeld = KeuzelijstField(naam="huidigNatuurbeeld",
                                                 label="huidig natuurbeeld",
                                                 lijst=KlNSB(),
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SoortenrijkSchraalGraslandGraslandfase5.huidigNatuurbeeld",
                                                 definition="Bepaling van het vegetatietype op basis van terreininventarisatie.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Bepaling van het vegetatietype op basis van terreininventarisatie."""
