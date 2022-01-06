from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlSleufUitvoering import KlSleufUitvoering
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Sleuf(AIMObject):
    """Lijnvormige verdieping van de natuurlijke ondergrond, nodig voor het leggen van leidingen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.breedte = KwantWrdInMeter()
        """De breedte van de sleuf in meter volgens figuur 7-1-1 van Standaardbestek 250."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf.breedte"
        self.breedte.definition = "De breedte van de sleuf in meter volgens figuur 7-1-1 van Standaardbestek 250."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""

        self.diepte = KwantWrdInMeter()
        """De diepte van de sleuf tussen toekomstig maaiveld en de binnenonderkant van de buis in meter."""
        self.diepte.naam = "diepte"
        self.diepte.label = "diepte"
        self.diepte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf.diepte"
        self.diepte.definition = "De diepte van de sleuf tussen toekomstig maaiveld en de binnenonderkant van de buis in meter."
        self.diepte.constraints = ""
        self.diepte.usagenote = ""
        self.diepte.deprecated_version = ""

        self.lengte = KwantWrdInMeter()
        """De totale lengte van de sleuf in lopende meter."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf.lengte"
        self.lengte.definition = "De totale lengte van de sleuf in lopende meter."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.uitvoering = KeuzelijstField(naam="uitvoering",
                                          label="uitvoering",
                                          lijst=KlSleufUitvoering(),
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf.uitvoering",
                                          definition="Bepaalt de wijze van de uitvoering van de sleuf.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Bepaalt de wijze van de uitvoering van de sleuf."""
