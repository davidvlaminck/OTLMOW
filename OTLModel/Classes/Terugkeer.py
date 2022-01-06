# coding=utf-8
from OTLModel.Classes.ComplexeGeleiding import ComplexeGeleiding
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlEcoOverstaptype import KlEcoOverstaptype


# Generated with OTLClassCreator. To modify: extend, do not edit
class Terugkeer(ComplexeGeleiding):
    """Een mogelijkheid om dieren die toch aan de wegkant verzeild zijn geraakt terug naar de veilige kant te laten begeven."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugkeer"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.typeUitvoering = KeuzelijstField(naam="typeUitvoering",
                                              label="type uitvoering",
                                              lijst=KlEcoOverstaptype(),
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugkeer.typeUitvoering",
                                              definition="Het type van terugkeer.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Het type van terugkeer."""
