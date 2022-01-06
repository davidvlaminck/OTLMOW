from abc import abstractmethod
from OTLModel.Classes.Detectielus import Detectielus
from OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class SelNietSelLus(Detectielus):
    """Abstracte klasse die de eigenschappen van selectieve en niet-selectieve lussen combineert."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.heeftMofInTrekput = BooleanField(naam="heeftMofInTrekput",
                                              label="heeft mof in trekput",
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus.heeftMofInTrekput",
                                              definition="Aanduiding of de mof bereikbaar is via een trekput.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Aanduiding of de mof bereikbaar is via een trekput."""

        self.isPrioritair = BooleanField(naam="isPrioritair",
                                         label="is prioritair",
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus.isPrioritair",
                                         definition="Geeft aan of de lus prioritair hersteld moet worden bij defect.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Geeft aan of de lus prioritair hersteld moet worden bij defect."""
