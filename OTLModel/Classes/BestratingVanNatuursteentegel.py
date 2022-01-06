from OTLModel.Classes.Bestrating import Bestrating
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBestratingAfwerking import KlBestratingAfwerking
from OTLModel.Datatypes.KlBestratingselementAfmetingLxB import KlBestratingselementAfmetingLxB
from OTLModel.Datatypes.KlNatuursteentegelGebruiksklasse import KlNatuursteentegelGebruiksklasse


# Generated with OTLClassCreator. To modify: extend, do not edit
class BestratingVanNatuursteentegel(Bestrating):
    """Een buitentegel (of buitenplavei) is elk element van natuursteen gebruikt als bestratingsmateriaal, waarvan de breedte groter is dan 150 mm en doorgaans groter is dan twee maal de dikte volgens PTV841."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.afmetingVanBestratingselementLxB = KeuzelijstField(naam="afmetingVanBestratingselementLxB",
                                                                label="afmeting van bestratingselement LxB",
                                                                lijst=KlBestratingselementAfmetingLxB(),
                                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel.afmetingVanBestratingselementLxB",
                                                                definition="De lengte en breedte van het bestratingselement in millimeter.",
                                                                constraints="",
                                                                usagenote="",
                                                                deprecated_version="")
        """De lengte en breedte van het bestratingselement in millimeter."""

        self.afwerking = KeuzelijstField(naam="afwerking",
                                         label="afwerking",
                                         lijst=KlBestratingAfwerking(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel.afwerking",
                                         definition="Bepaling van de afwerking van het oppervlak van de natuursteentegels.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Bepaling van de afwerking van het oppervlak van de natuursteentegels."""

        self.gebruiksklasse = KeuzelijstField(naam="gebruiksklasse",
                                              label="gebruiksklasse",
                                              lijst=KlNatuursteentegelGebruiksklasse(),
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel.gebruiksklasse",
                                              definition="Bepaling van het toegelaten verkeer en belasting op de bestrating van natuursteentegels.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Bepaling van het toegelaten verkeer en belasting op de bestrating van natuursteentegels."""
