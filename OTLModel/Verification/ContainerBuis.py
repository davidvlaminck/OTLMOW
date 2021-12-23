from abc import abstractmethod, ABC
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.StringField import StringField


class ContainerBuis(ABC):
    """Abstracte voor het groeperen van eigenschappen en relaties van buisvormige container elementen. Dit zijn buizen die
    kabels of andere leidingen kunnen bevatten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        kleurField = StringField(naam="kleur",
                                 label="kleur",
                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis.kleur",
                                 definition="De kleur van de coating.",
                                 constraints="",
                                 usagenote="",
                                 deprecated_version="")
        self.kleur = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=kleurField)
        """De kleur van de coating."""
