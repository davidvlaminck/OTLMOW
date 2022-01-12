# coding=utf-8
from OTLModel.Classes.ComplexeGeleiding import ComplexeGeleiding
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlEcoPaalmateriaal import KlEcoPaalmateriaal
from OTLModel.Datatypes.KlRasterMazen import KlRasterMazen
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ecoraster(ComplexeGeleiding):
    """Een geleiding om dieren te leiden naar een plaats (ecoduct, ecotunnel, ...) waar ze veilig een drukke weg kunnen oversteken."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.heeftPrikkeldraad = BooleanField(naam="heeftPrikkeldraad",
                                              label="heeft prikkeldraad",
                                              objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.heeftPrikkeldraad",
                                              definition="Aanduiding of het ecoraster is voorzien van prikkeldraad.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Aanduiding of het ecoraster is voorzien van prikkeldraad."""

        self.heeftSpandraden = BooleanField(naam="heeftSpandraden",
                                            label="heeft spandraden",
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.heeftSpandraden",
                                            definition="Aanduiding of het ecoraster is voorzien van spandraden.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Aanduiding of het ecoraster is voorzien van spandraden."""

        self.lengte = KwantWrdInMeter()
        """De lengte van het ecoraster in meter."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.lengte"
        self.lengte.definition = "De lengte van het ecoraster in meter."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.paalhoogte = KwantWrdInMeter()
        """De hoogte van de paal in het ecoraster in meter."""
        self.paalhoogte.naam = "paalhoogte"
        self.paalhoogte.label = "paalhoogte"
        self.paalhoogte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.paalhoogte"
        self.paalhoogte.definition = "De hoogte van de paal in het ecoraster in meter."
        self.paalhoogte.constraints = ""
        self.paalhoogte.usagenote = ""
        self.paalhoogte.deprecated_version = ""

        self.paalMateriaal = KeuzelijstField(naam="paalMateriaal",
                                             label="paal materiaal",
                                             lijst=KlEcoPaalmateriaal(),
                                             objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.paalMateriaal",
                                             definition="Het materiaal van de paal in het ecoraster.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Het materiaal van de paal in het ecoraster."""

        self.typeMazen = KeuzelijstField(naam="typeMazen",
                                         label="type mazen",
                                         lijst=KlRasterMazen(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.typeMazen",
                                         definition="Het type van de mazen in het ecoraster.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Het type van de mazen in het ecoraster."""
