from OTLModel.Classes.AndereVerharding import AndereVerharding
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlSteenslagType import KlSteenslagType


# Generated with OTLClassCreator
class Steenslagverharding(AndereVerharding):
    """Een verharding van gebroken steen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Steenslagverharding"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlSteenslagType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Steenslagverharding.type",
                                    definition="Bepaling van het type steenslagverharding.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Bepaling van het type steenslagverharding."""
