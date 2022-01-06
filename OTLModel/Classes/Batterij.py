from OTLModel.Classes.Voedingspunt import Voedingspunt
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBatterijMerk import KlBatterijMerk
from OTLModel.Datatypes.KlBatterijModelnaam import KlBatterijModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Batterij(Voedingspunt):
    """Element bestaande uit meerdere elektrochemische cellen voor het leveren van elektriciteit,die ontstaat door de omzetting van opgeslagen chemische energie in elektrische energie."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlBatterijMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij.merk",
                                    definition="Merk van de batterij.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merk van de batterij."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlBatterijModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij.modelnaam",
                                         definition="Modelnaam van de batterij.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Modelnaam van de batterij."""
