from OTLModel.Classes.Ruigte import Ruigte
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlNSB import KlNSB


# Generated with OTLClassCreator
class VerruigdGrasland(Ruigte):
    """R2 - grote brandnetel, kleefkruid, ridderzuring, akkerdistel, speerdistel, gewone berenklauw, fluitenkruid, bramen, klit, jacobskruiskruid, ijle dravik, dolle kervel, kweek, kropaar, haagwinde, zevenblad."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerruigdGrasland"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.huidigNatuurbeeld = KeuzelijstField(naam="huidigNatuurbeeld",
                                                 label="huidig natuurbeeld",
                                                 lijst=KlNSB(),
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerruigdGrasland.huidigNatuurbeeld",
                                                 definition="Bepaling van het vegetatietype op basis van terreininventarisatie.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Bepaling van het vegetatietype op basis van terreininventarisatie."""
