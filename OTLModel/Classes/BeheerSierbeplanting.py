from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBeheerSierbeplanting import KlBeheerSierbeplanting
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator
class BeheerSierbeplanting(AIMObject):
    """Het beheerobject voor de sierbeplanting."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerSierbeplanting"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        beheeroptieField = KeuzelijstField(naam="beheeroptie",
                                           label="beheeroptie",
                                           lijst=KlBeheerSierbeplanting(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerSierbeplanting.beheeroptie",
                                           definition="Aanduiding van welk beheer wordt toegepast op de sierbeplanting.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        self.beheeroptie = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=beheeroptieField)
        """Aanduiding van welk beheer wordt toegepast op de sierbeplanting."""

        self.heeftBeheerplan = BooleanField(naam="heeftBeheerplan",
                                            label="heeft beheerplan",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerSierbeplanting.heeftBeheerplan",
                                            definition="Aanduiding of er een beheerplan bestaat.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Aanduiding of er een beheerplan bestaat."""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte in vierkante meter van de te behandelen sierbeplanting."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerSierbeplanting.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte in vierkante meter van de te behandelen sierbeplanting."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""
