# coding=utf-8
from OTLModel.Classes.Straatmeubilair import Straatmeubilair
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlKleurPlooibaken import KlKleurPlooibaken
from OTLModel.Datatypes.KlPlooibakenType import KlPlooibakenType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Plooibaken(Straatmeubilair):
    """Een zacht kunststoffen paal met verschillende diameter en reflecterende banden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Plooibaken"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.kleur = KeuzelijstField(naam="kleur",
                                     label="kleur",
                                     lijst=KlKleurPlooibaken(),
                                     objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Plooibaken.kleur",
                                     definition="Bepaling van de kleur van het plooibaken.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """Bepaling van de kleur van het plooibaken."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlPlooibakenType(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Plooibaken.type",
                                    definition="De diameter en vorm van het plooibaken.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De diameter en vorm van het plooibaken."""
