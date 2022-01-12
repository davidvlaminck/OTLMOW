# coding=utf-8
from OTLModel.Classes.Markering import Markering
from OTLModel.Classes.AOWSType import AOWSType
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlGekleurdWVCode import KlGekleurdWVCode
from OTLModel.Datatypes.KlGekleurdWVSoort import KlGekleurdWVSoort
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class GekleurdWegvlakMarkering(Markering, AOWSType):
    """Een markering van een wegdeel aangebracht om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GekleurdWegvlakMarkering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Markering.__init__(self)
        AOWSType.__init__(self)

        self.breedte = KwantWrdInMeter()
        """De breedte van de markering in meter."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GekleurdWegvlakMarkering.breedte"
        self.breedte.definition = "De breedte van de markering in meter."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""

        self.code = KeuzelijstField(naam="code",
                                    label="code",
                                    lijst=KlGekleurdWVCode(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GekleurdWegvlakMarkering.code",
                                    definition="De  (COPRO/BENOR) code van de gekleurde wegvlak markering.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De  (COPRO/BENOR) code van de gekleurde wegvlak markering."""

        self.lengte = KwantWrdInMeter()
        """De lengte van de markering in meter."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GekleurdWegvlakMarkering.lengte"
        self.lengte.definition = "De lengte van de markering in meter."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte van het gekleurd wegdeel in vierkante meter."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GekleurdWegvlakMarkering.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte van het gekleurd wegdeel in vierkante meter."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""

        self.soortOmschrijving = KeuzelijstField(naam="soortOmschrijving",
                                                 label="soort omschrijving",
                                                 lijst=KlGekleurdWVSoort(),
                                                 objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GekleurdWegvlakMarkering.soortOmschrijving",
                                                 definition="De soort en tevens omschrijving van de figuratie markering.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """De soort en tevens omschrijving van de figuratie markering."""
