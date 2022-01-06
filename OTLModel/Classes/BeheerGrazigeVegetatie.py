from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcMaaien import DtcMaaien
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBeheerGrazigeVegetatie import KlBeheerGrazigeVegetatie
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class BeheerGrazigeVegetatie(AIMObject):
    """Het beheerobject voor de grazige vegetatie."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        beheeroptieField = KeuzelijstField(naam="beheeroptie",
                                           label="beheeroptie",
                                           lijst=KlBeheerGrazigeVegetatie(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie.beheeroptie",
                                           definition="Aanduiding van welk beheer wordt toegepast op de grazige vegetatie.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        self.beheeroptie = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=beheeroptieField)
        """Aanduiding van welk beheer wordt toegepast op de grazige vegetatie."""

        self.heeftBeheerplan = BooleanField(naam="heeftBeheerplan",
                                            label="heeft beheerplan",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie.heeftBeheerplan",
                                            definition="Aanduiding of er een beheerplan bestaat.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Aanduiding of er een beheerplan bestaat."""

        self.lengte = KwantWrdInMeter()
        """De lengte in meter van de te behandelen grazige vegetatie."""
        self.lengte.naam = "lengte"
        self.lengte.label = "Lengte"
        self.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie.lengte"
        self.lengte.definition = "De lengte in meter van de te behandelen grazige vegetatie."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.maaien = DtcMaaien()
        """Complex datatype voor de eigenschappen van maaien."""
        self.maaien.naam = "maaien"
        self.maaien.label = "maaien"
        self.maaien.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie.maaien"
        self.maaien.definition = "Complex datatype voor de eigenschappen van maaien."
        self.maaien.constraints = ""
        self.maaien.usagenote = ""
        self.maaien.deprecated_version = ""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte in vierkante meter van de te behandelen grazige vegetatie."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte in vierkante meter van de te behandelen grazige vegetatie."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""
