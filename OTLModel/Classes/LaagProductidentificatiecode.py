from abc import abstractmethod, ABC
from OTLModel.Datatypes.DtcProductidentificatiecode import DtcProductidentificatiecode


# Generated with OTLClassCreator
class LaagProductidentificatiecode(ABC):
    """Abstracte waarmee aan een laag de eigenschap productidentificatiecode wordt toegekend."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagProductidentificatiecode"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.productidentificatiecode = DtcProductidentificatiecode()
        """De productidentificatiecode van het gebruikte product (bv. COPRO code of Benor code)."""
        self.productidentificatiecode.naam = "productidentificatiecode"
        self.productidentificatiecode.label = "productidentificatiecode"
        self.productidentificatiecode.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagProductidentificatiecode.productidentificatiecode"
        self.productidentificatiecode.definition = "De productidentificatiecode van het gebruikte product (bv. COPRO code of Benor code)."
        self.productidentificatiecode.constraints = ""
        self.productidentificatiecode.usagenote = ""
        self.productidentificatiecode.deprecated_version = ""
