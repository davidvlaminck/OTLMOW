from abc import abstractmethod, ABC

from OTLModel.Datatypes.BooleanField import BooleanField


class AIMDBStatus(ABC):
    """Voegt een attribuut toe aan de subklasse dat aangeeft of de asset zichtbaar is in de databank of (zacht) verwijderd is."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus"

    @abstractmethod
    def __init__(self):
        self.isActief = BooleanField(naam="isActief", label="is actief",
                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus.isActief",
                            definition="Geeft aan of het object actief kan gebruikt worden of (zacht) verwijderd is uit het asset beheer systeem."
                            , constraints="", usagenote="", deprecated_version="")
        """Geeft aan of het object actief kan gebruikt worden of (zacht) verwijderd is uit het asset beheer systeem."""