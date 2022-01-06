from abc import abstractmethod, ABC
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAIMToestand import KlAIMToestand


# Generated with OTLClassCreator. To modify: extend, do not edit
class AIMToestand(ABC):
    """Voegt een attribuut toe aan de subklasse dat de huidige stand in de levenscyclus van het object aangeeft."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.toestand = KeuzelijstField(naam="toestand",
                                        label="toestand",
                                        lijst=KlAIMToestand(),
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand.toestand",
                                        definition="Geeft de actuele stand in de levenscyclus van het object.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Geeft de actuele stand in de levenscyclus van het object."""
