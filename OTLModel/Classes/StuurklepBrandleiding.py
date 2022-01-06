from OTLModel.Classes.Brandvoorziening import Brandvoorziening
from OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class StuurklepBrandleiding(Brandvoorziening):
    """Een afsluiter die vanop afstand bediend wordt om te verhinderen dat er water in de leiding blijft staan."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StuurklepBrandleiding"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.heeftLeegloopklep = BooleanField(naam="heeftLeegloopklep",
                                              label="heeft leegloopklep",
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StuurklepBrandleiding.heeftLeegloopklep",
                                              definition="Voorziet een mogelijkheid om via de klep de brandleiding te laten leeglopen.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Voorziet een mogelijkheid om via de klep de brandleiding te laten leeglopen."""
