# coding=utf-8
from OTLModel.Classes.Bestrating import Bestrating
from OTLModel.Datatypes.DtcBSSRandafwerking import DtcBSSRandafwerking
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBSSType import KlBSSType
from OTLModel.Datatypes.KlBestratingAfwerking import KlBestratingAfwerking
from OTLModel.Datatypes.KlBestratingselementAfmetingLxB import KlBestratingselementAfmetingLxB


# Generated with OTLClassCreator. To modify: extend, do not edit
class BestratingVanBetonstraatsteen(Bestrating):
    """Bestrating van geprefabriceerde stenen in beton die (in de afgesproken mate) voldoen aan de vereisten van NBN EN 1338 en NBN B21-311."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetonstraatsteen"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.afmetingVanBestratingselementLxB = KeuzelijstField(naam="afmetingVanBestratingselementLxB",
                                                                label="afmeting van bestratingselement LxB",
                                                                lijst=KlBestratingselementAfmetingLxB(),
                                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetonstraatsteen.afmetingVanBestratingselementLxB",
                                                                definition="De lengte en breedte van het bestratingselement in millimeter.",
                                                                constraints="",
                                                                usagenote="",
                                                                deprecated_version="")
        """De lengte en breedte van het bestratingselement in millimeter."""

        self.afwerking = KeuzelijstField(naam="afwerking",
                                         label="afwerking",
                                         lijst=KlBestratingAfwerking(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetonstraatsteen.afwerking",
                                         definition="Bepaling van afwerking van de betonstraatstenen.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Bepaling van afwerking van de betonstraatstenen."""

        self.randafwerking = DtcBSSRandafwerking()
        """De wijze waarop de rand van de betonstraatsteenverharding is afgewerkt."""
        self.randafwerking.naam = "randafwerking"
        self.randafwerking.label = "randafwerking"
        self.randafwerking.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetonstraatsteen.randafwerking"
        self.randafwerking.definition = "De wijze waarop de rand van de betonstraatsteenverharding is afgewerkt."
        self.randafwerking.constraints = ""
        self.randafwerking.usagenote = ""
        self.randafwerking.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlBSSType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetonstraatsteen.type",
                                    definition="Het type betonstraatsteen.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type betonstraatsteen."""
