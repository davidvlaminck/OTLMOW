from OTLModel.Classes.Bestrating import Bestrating
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBSSType import KlBSSType
from OTLModel.Datatypes.KlBestratingAfwerking import KlBestratingAfwerking
from OTLModel.Datatypes.KlBestratingselementAfmetingLxB import KlBestratingselementAfmetingLxB


# Generated with OTLClassCreator
class BestratingVanBetontegel(Bestrating):
    """Bestrating van geprefabriceerde platte stenen in beton die (in de afgesproken mate) voldoen aan de vereisten van NBN EN 1339 en NBN B21-211."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetontegel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.afmetingVanBestratingselementLxB = KeuzelijstField(naam="afmetingVanBestratingselementLxB",
                                                                label="afmeting van bestratingselement LxB",
                                                                lijst=KlBestratingselementAfmetingLxB(),
                                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetontegel.afmetingVanBestratingselementLxB",
                                                                definition="De lengte en breedte van het bestratingselement in millimeter.",
                                                                constraints="",
                                                                usagenote="",
                                                                deprecated_version="")
        """De lengte en breedte van het bestratingselement in millimeter."""

        self.afwerking = KeuzelijstField(naam="afwerking",
                                         label="afwerking",
                                         lijst=KlBestratingAfwerking(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetontegel.afwerking",
                                         definition="Bepaling van afwerking van de betontegels.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Bepaling van afwerking van de betontegels."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlBSSType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetontegel.type",
                                    definition="Het type betontegel.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type betontegel."""
