from OTLModel.Classes.ConstructieElement import ConstructieElement
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDamwandMateriaal import KlDamwandMateriaal
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator
class Damwand(ConstructieElement):
    """Een grond- en/of waterkerende constructie, die bestaat uit een verticaal in de grond geplaatste wand."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.isWaterdicht = BooleanField(naam="isWaterdicht",
                                         label="is waterdicht",
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand.isWaterdicht",
                                         definition="Geeft aan of de damwand al dan niet waterdicht is.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Geeft aan of de damwand al dan niet waterdicht is."""

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="Damwand materiaal",
                                         lijst=KlDamwandMateriaal(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand.materiaal",
                                         definition="Het materiaal waaruit de damwand bestaat.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Het materiaal waaruit de damwand bestaat."""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De totale oppervlakte van de damwandconstructie in vierkante meter."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand.oppervlakte"
        self.oppervlakte.definition = "De totale oppervlakte van de damwandconstructie in vierkante meter."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""

        self.profiellengte = KwantWrdInMeter()
        """De lengte van één damwandprofiel."""
        self.profiellengte.naam = "profiellengte"
        self.profiellengte.label = "profiellengte"
        self.profiellengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand.profiellengte"
        self.profiellengte.definition = "De lengte van één damwandprofiel."
        self.profiellengte.constraints = ""
        self.profiellengte.usagenote = ""
        self.profiellengte.deprecated_version = ""

        self.totaleLengte = KwantWrdInMeter()
        """De totale lengte van de damwandconstructie in lopende meter."""
        self.totaleLengte.naam = "totaleLengte"
        self.totaleLengte.label = "totale lengte"
        self.totaleLengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand.totaleLengte"
        self.totaleLengte.definition = "De totale lengte van de damwandconstructie in lopende meter."
        self.totaleLengte.constraints = ""
        self.totaleLengte.usagenote = ""
        self.totaleLengte.deprecated_version = ""
