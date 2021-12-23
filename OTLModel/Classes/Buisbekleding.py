from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBekledingPlaats import KlBekledingPlaats
from OTLModel.Datatypes.KlBuisbekledingUitvoeringswijze import KlBuisbekledingUitvoeringswijze
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator
class Buisbekleding(AIMObject):
    """De bekleding of coating ter bescherming van de buis."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.laagdikte = KwantWrdInMillimeter()
        """De dikte van de bekledingslaag in millimeter."""
        self.laagdikte.naam = "laagdikte"
        self.laagdikte.label = "Laagdikte"
        self.laagdikte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.laagdikte"
        self.laagdikte.definition = "De dikte van de bekledingslaag in millimeter."
        self.laagdikte.constraints = ""
        self.laagdikte.usagenote = ""
        self.laagdikte.deprecated_version = ""

        self.lengte = KwantWrdInMeter()
        """De totale lengte van de buisbekleding in lopende meter."""
        self.lengte.naam = "lengte"
        self.lengte.label = "Lengte"
        self.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.lengte"
        self.lengte.definition = "De totale lengte van de buisbekleding in lopende meter."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.plaats = KeuzelijstField(naam="plaats",
                                      label="plaats",
                                      lijst=KlBekledingPlaats(),
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.plaats",
                                      definition="De kant waar de bekleding van de buis zich bevindt.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """De kant waar de bekleding van de buis zich bevindt."""

        self.technischeFiche = DtcDocument()
        """De technische fiche van de buisbekleding."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.technischeFiche"
        self.technischeFiche.definition = "De technische fiche van de buisbekleding."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""

        self.tot = KwantWrdInMeter()
        """Het einde van de buisbekleding in meter ten opzichte van de beginput van de buis."""
        self.tot.naam = "tot"
        self.tot.label = "tot"
        self.tot.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.tot"
        self.tot.definition = "Het einde van de buisbekleding in meter ten opzichte van de beginput van de buis."
        self.tot.constraints = ""
        self.tot.usagenote = ""
        self.tot.deprecated_version = ""

        self.uitvoeringswijze = KeuzelijstField(naam="uitvoeringswijze",
                                                label="uitvoeringswijze",
                                                lijst=KlBuisbekledingUitvoeringswijze(),
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.uitvoeringswijze",
                                                definition="Materiaal en manier van aanbrengen van de buisbekleding.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Materiaal en manier van aanbrengen van de buisbekleding."""

        self.van = KwantWrdInMeter()
        """Het begin van de buisbekleding in meter ten opzichte van de beginput van de leiding."""
        self.van.naam = "van"
        self.van.label = "van"
        self.van.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.van"
        self.van.definition = "Het begin van de buisbekleding in meter ten opzichte van de beginput van de leiding."
        self.van.constraints = ""
        self.van.usagenote = ""
        self.van.deprecated_version = ""
