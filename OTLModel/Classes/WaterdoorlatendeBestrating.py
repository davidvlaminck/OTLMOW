# coding=utf-8
from OTLModel.Classes.Bestrating import Bestrating
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAardWBSS import KlAardWBSS
from OTLModel.Datatypes.KlBestratingAfwerking import KlBestratingAfwerking
from OTLModel.Datatypes.KlBestratingselementAfmetingLxB import KlBestratingselementAfmetingLxB
from OTLModel.Datatypes.KlWBSSType import KlWBSSType


# Generated with OTLClassCreator. To modify: extend, do not edit
class WaterdoorlatendeBestrating(Bestrating):
    """Betonstraatstenen of betontegels die omwille van hun vormkenmerken (bv. drainageopeningen of verbrede voegen) of betonstructuur (poreus beton met een open korrelopbouw) water doorlaten zoals omschreven in PTV 122."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.aard = KeuzelijstField(naam="aard",
                                    label="aard",
                                    lijst=KlAardWBSS(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.aard",
                                    definition="Het kenmerk of de vorm van de waterdoorlatende betonstraatsteen waardoor infiltratie van hemelwater in de bodem mogelijk is.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het kenmerk of de vorm van de waterdoorlatende betonstraatsteen waardoor infiltratie van hemelwater in de bodem mogelijk is."""

        self.afmetingVanBestratingselementLxB = KeuzelijstField(naam="afmetingVanBestratingselementLxB",
                                                                label="afmeting van bestratingselement LxB",
                                                                lijst=KlBestratingselementAfmetingLxB(),
                                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.afmetingVanBestratingselementLxB",
                                                                definition="De lengte en breedte van het bestratingselement in millimeter.",
                                                                constraints="",
                                                                usagenote="",
                                                                deprecated_version="")
        """De lengte en breedte van het bestratingselement in millimeter."""

        self.afwerking = KeuzelijstField(naam="afwerking",
                                         label="afwerking",
                                         lijst=KlBestratingAfwerking(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.afwerking",
                                         definition="Bepaling van de afwerking van de waterdoorlatende betonstraatstenen of betontegels.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Bepaling van de afwerking van de waterdoorlatende betonstraatstenen of betontegels."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlWBSSType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.type",
                                    definition="Het type van waterdoorlatende betonstraatstenen of betontegels.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van waterdoorlatende betonstraatstenen of betontegels."""
