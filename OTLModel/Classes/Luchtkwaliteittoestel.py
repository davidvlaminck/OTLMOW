from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLuchtkwaliteitOpstellingMerk import KlLuchtkwaliteitOpstellingMerk
from OTLModel.Datatypes.KlLuchtkwaliteitOpstellingModelnaam import KlLuchtkwaliteitOpstellingModelnaam


# Generated with OTLClassCreator
class Luchtkwaliteittoestel(AIMNaamObject):
    """Abstracte voor attributen van onderdelen van de luchtkwaliteitsensor installatie."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Luchtkwaliteittoestel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlLuchtkwaliteitOpstellingMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Luchtkwaliteittoestel.merk",
                                    definition="Het merk van een onderdeel uit een luchtkwaliteitsinstallatie.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van een onderdeel uit een luchtkwaliteitsinstallatie."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlLuchtkwaliteitOpstellingModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Luchtkwaliteittoestel.modelnaam",
                                         definition="De modelnaam van een onderdeel uit een luchtkwaliteitsinstallatie.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van een onderdeel uit een luchtkwaliteitsinstallatie."""
