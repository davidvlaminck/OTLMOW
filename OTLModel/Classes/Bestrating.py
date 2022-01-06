# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.ArtificieleLaag import ArtificieleLaag
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBestratingSteenverband import KlBestratingSteenverband
from OTLModel.Datatypes.KlBestratingVoegvulling import KlBestratingVoegvulling
from OTLModel.Datatypes.KlKleurSupp import KlKleurSupp


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bestrating(ArtificieleLaag):
    """Verhardingstype opgebouwd uit bestratingen (rechthoekige of vierkante componenten van beperkte afmetingen) waardoor een aanzienlijk aantal voegen tussen de componenten zitten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.kleur = KeuzelijstField(naam="kleur",
                                     label="kleur",
                                     lijst=KlKleurSupp(),
                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating.kleur",
                                     definition="De kleur van de bestrating.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """De kleur van de bestrating."""

        self.steenverband = KeuzelijstField(naam="steenverband",
                                            label="steenverband",
                                            lijst=KlBestratingSteenverband(),
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating.steenverband",
                                            definition="Het patroon waarin de bestrating gelegd werd.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Het patroon waarin de bestrating gelegd werd."""

        self.voegvulling = KeuzelijstField(naam="voegvulling",
                                           label="voegvulling",
                                           lijst=KlBestratingVoegvulling(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating.voegvulling",
                                           definition="De gebruikte voegvulling van de bestrating.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """De gebruikte voegvulling van de bestrating."""
