from OTLModel.Classes.Bebakening import Bebakening
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlWegreflectorType import KlWegreflectorType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wegreflector(Bebakening):
    """Heeft als doel de zichtbaarheid van verkeerseilanden te verhogen en geleiding van de weggebruiker langs de weg."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegreflector"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlWegreflectorType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegreflector.type",
                                    definition="De vorm van wegreflector.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De vorm van wegreflector."""
