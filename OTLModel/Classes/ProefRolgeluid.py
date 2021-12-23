from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator
class ProefRolgeluid(Proef):
    """Het rolgeluid wordt gemeten met de CPX-methode volgens ISO/CEN 11819-2."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefRolgeluid"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.rolgeluid = DtcDocument()
        """Proefresultaten van het rolgeluid van de toplaag."""
        self.rolgeluid.naam = "rolgeluid"
        self.rolgeluid.label = "rolgeluid"
        self.rolgeluid.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefRolgeluid.rolgeluid"
        self.rolgeluid.definition = "Proefresultaten van het rolgeluid van de toplaag."
        self.rolgeluid.constraints = ""
        self.rolgeluid.usagenote = ""
        self.rolgeluid.deprecated_version = ""
