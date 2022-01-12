# coding=utf-8
from OTLModel.Classes.VRIDraagconstructie import VRIDraagconstructie
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBoogpaalType import KlBoogpaalType


# Generated with OTLClassCreator. To modify: extend, do not edit
class BoogpaalVerkeerslicht(VRIDraagconstructie):
    """Paal bestemd voor het bevestigen van seinlantaarns boven het wegdek. Geschikt voor het bevestigen van ten hoogste 4 seinlantaarns van het type 300 en van één of meerdere lantaarns van het type 200 op de paalschacht. De vrije hoogte ten opzichte van het wegdek bedraagt onder de lantaarns 6.500 millimeter voor palen met grote draagwijdte (7,5 meter overspanning) en 5.500 millimeter voor de palen met middelgrote draagwijdte (3,5 meter overspanning)."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BoogpaalVerkeerslicht"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.typeBoogpaal = KeuzelijstField(naam="typeBoogpaal",
                                            label="type boogpaal",
                                            lijst=KlBoogpaalType(),
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BoogpaalVerkeerslicht.typeBoogpaal",
                                            definition="Draagwijdte van de boogpaal.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Draagwijdte van de boogpaal."""
