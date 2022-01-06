# coding=utf-8
from OTLModel.Classes.Buis import Buis
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDraineerbuisMateriaal import KlDraineerbuisMateriaal


# Generated with OTLClassCreator. To modify: extend, do not edit
class Draineerbuis(Buis):
    """Een buis voor het afvoeren van water uit de bodem over en door de grond,met als gevolg het verlagen van het grondwaterpeil."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerbuis"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.heeftDrainbrug = BooleanField(naam="heeftDrainbrug",
                                           label="heeft drainbrug",
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerbuis.heeftDrainbrug",
                                           definition="Aanduiding of er al dan niet een profiel onderaan de draineerbuis aanwezig is om zettingen te vermijden.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Aanduiding of er al dan niet een profiel onderaan de draineerbuis aanwezig is om zettingen te vermijden."""

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlDraineerbuisMateriaal(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerbuis.materiaal",
                                         definition="Bepaalt het materiaal van de draineerbuis.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Bepaalt het materiaal van de draineerbuis."""
