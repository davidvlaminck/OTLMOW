# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBeheerBoomvorm import KlBeheerBoomvorm
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class BeheerBoomvorm(AIMObject):
    """Het beheerobject voor de solitaire boom."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerBoomvorm"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        beheeroptieField = KeuzelijstField(naam="beheeroptie",
                                           label="beheeroptie",
                                           lijst=KlBeheerBoomvorm(),
                                           objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerBoomvorm.beheeroptie",
                                           definition="Behandelingswijzen van bomen.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        self.beheeroptie = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=beheeroptieField)
        """Behandelingswijzen van bomen."""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte in vierkante meter van de te behandelen grond rond de boom."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerBoomvorm.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte in vierkante meter van de te behandelen grond rond de boom."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""
