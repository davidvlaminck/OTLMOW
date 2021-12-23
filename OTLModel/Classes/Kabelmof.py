from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlKabelmofType import KlKabelmofType


# Generated with OTLClassCreator
class Kabelmof(AIMNaamObject):
    """Een verbindingsgreep die aansluitingen van kabels rondom afsluit."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.type = KeuzelijstField(naam="type",
                                    label="type kabelmof",
                                    lijst=KlKabelmofType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof.type",
                                    definition="Soort mof volgens een lijst van types.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Soort mof volgens een lijst van types."""
