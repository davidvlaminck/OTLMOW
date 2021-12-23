from abc import abstractmethod, ABC
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator
class FirmwareObject(ABC):
    """Abstracte voor de firmware van het object."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#FirmwareObject"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.firmwareversie = StringField(naam="firmwareversie",
                                          label="firmwareversie",
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#FirmwareObject.firmwareversie",
                                          definition="Versie van de firmware.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Versie van de firmware."""
