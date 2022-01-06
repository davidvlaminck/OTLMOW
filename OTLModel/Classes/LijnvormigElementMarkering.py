# coding=utf-8
from OTLModel.Classes.Markering import Markering
from OTLModel.Classes.AOWSType import AOWSType
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEMarkeringCode import KlLEMarkeringCode
from OTLModel.Datatypes.KlLEMarkeringSoort import KlLEMarkeringSoort
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class LijnvormigElementMarkering(Markering, AOWSType):
    """Een markering van een lijnvormig element om de zichtbaarheid te verhogen om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LijnvormigElementMarkering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Markering.__init__(self)
        AOWSType.__init__(self)

        self.code = KeuzelijstField(naam="code",
                                    label="code",
                                    lijst=KlLEMarkeringCode(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LijnvormigElementMarkering.code",
                                    definition="De (COPRO/BENOR) code van de lijnvormig element markering.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De (COPRO/BENOR) code van de lijnvormig element markering."""

        self.lengte = KwantWrdInMeter()
        """De lengte van de markering in meter."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LijnvormigElementMarkering.lengte"
        self.lengte.definition = "De lengte van de markering in meter."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte van de markering op het lijnvormig element in vierkante meter."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LijnvormigElementMarkering.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte van de markering op het lijnvormig element in vierkante meter."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""

        self.soortOmschrijving = KeuzelijstField(naam="soortOmschrijving",
                                                 label="soort omschrijving",
                                                 lijst=KlLEMarkeringSoort(),
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LijnvormigElementMarkering.soortOmschrijving",
                                                 definition="De soort en tevens de omschrijving van de lijnvormige elementen markering.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """De soort en tevens de omschrijving van de lijnvormige elementen markering."""
