from abc import abstractmethod, ABC
from OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class AIMDBStatus(ABC):
    """Voegt een attribuut toe aan de subklasse dat aangeeft of de asset zichtbaar is in de databank of (zacht) verwijderd is."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.isActief = BooleanField(naam="isActief",
                                     label="is actief",
                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus.isActief",
                                     definition="Geeft aan of het object actief kan gebruikt worden of (zacht) verwijderd is uit het asset beheer systeem.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """Geeft aan of het object actief kan gebruikt worden of (zacht) verwijderd is uit het asset beheer systeem."""
