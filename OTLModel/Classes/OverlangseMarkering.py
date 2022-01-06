# coding=utf-8
from OTLModel.Classes.Markering import Markering
from OTLModel.Classes.AOWSType import AOWSType
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlOverlangseMarkeringCode import KlOverlangseMarkeringCode
from OTLModel.Datatypes.KlOverlangsemarkeringType import KlOverlangsemarkeringType
from OTLModel.Datatypes.KlPositieSoort import KlPositieSoort
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class OverlangseMarkering(Markering, AOWSType):
    """Een markering overlangs op de weg aangebracht om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Markering.__init__(self)
        AOWSType.__init__(self)

        self.code = KeuzelijstField(naam="code",
                                    label="code",
                                    lijst=KlOverlangseMarkeringCode(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering.code",
                                    definition="De (COPRO/BENOR) code van de overlangse markering.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De (COPRO/BENOR) code van de overlangse markering."""

        self.lengte = KwantWrdInMeter()
        """De lengte van de markering in meter."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering.lengte"
        self.lengte.definition = "De lengte van de markering in meter."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte van de overlangse markering in vierkante meter."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte van de overlangse markering in vierkante meter."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""

        self.positie = KeuzelijstField(naam="positie",
                                       label="positie",
                                       lijst=KlPositieSoort(),
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering.positie",
                                       definition="Bepaling van het wegdeel van de overlangse markering.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Bepaling van het wegdeel van de overlangse markering."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlOverlangsemarkeringType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering.type",
                                    definition="Het type van overlangse markering.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van overlangse markering."""
