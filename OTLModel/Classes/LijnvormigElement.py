from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class LijnvormigElement(AIMObject):
    """Abstracte voor de gemeenschappelijke eigenschappen en relaties van lijnvormige elementen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        technischeFicheField = DtcDocument()
        technischeFicheField.naam = "technischeFiche"
        technischeFicheField.label = "technische fiche"
        technischeFicheField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement.technischeFiche"
        technischeFicheField.definition = "De technische fiche van het lijnvormig element."
        technischeFicheField.constraints = ""
        technischeFicheField.usagenote = ""
        technischeFicheField.deprecated_version = ""
        self.technischeFiche = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=technischeFicheField)
        """De technische fiche van het lijnvormig element."""
