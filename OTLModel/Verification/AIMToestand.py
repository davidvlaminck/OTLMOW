from abc import ABC, abstractmethod

from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Verification.KlAIMToestand import KlAIMToestand


class AIMToestand(ABC):
    """Voegt een attribuut toe aan de subklasse dat de huidige stand in de levenscyclus van het object aangeeft."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.toestand = KeuzelijstField(lijst=KlAIMToestand(),
                                        naam="toestand",
                                        label="toestand",
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand.toestand",
                                        definition="Geeft de actuele stand in de levenscyclus van het object.",
                                        overerving=False,
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Geeft de actuele stand in de levenscyclus van het object."""


