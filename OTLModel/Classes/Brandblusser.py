from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBrandblusserBlusmiddel import KlBrandblusserBlusmiddel
from OTLModel.Datatypes.KlBrandblusserGewicht import KlBrandblusserGewicht
from OTLModel.Datatypes.KlBrandblusserType import KlBrandblusserType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brandblusser(AIMObject):
    """Een apparaat om het vuur van een kleine brand mee te doven. Het bestaat uit een cilinder waarin een beperkte hoeveelheid blusmiddel onder druk staat."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.aankoopdatum = DateField(naam="aankoopdatum",
                                      label="aankoopdatum",
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.aankoopdatum",
                                      definition="Datum wordt het toestel is aangekocht.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """Datum wordt het toestel is aangekocht."""

        self.blusmiddel = KeuzelijstField(naam="blusmiddel",
                                          label="blusmiddel",
                                          lijst=KlBrandblusserBlusmiddel(),
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.blusmiddel",
                                          definition="Substantie waarmee het toestel gevuld is in functie van het blussen van vuur.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Substantie waarmee het toestel gevuld is in functie van het blussen van vuur."""

        self.gewicht = KeuzelijstField(naam="gewicht",
                                       label="gewicht",
                                       lijst=KlBrandblusserGewicht(),
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.gewicht",
                                       definition="Totaal gewicht van het gevulde toestel.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Totaal gewicht van het gevulde toestel."""

        self.keuringsdatum = DateField(naam="keuringsdatum",
                                       label="keuringsdatum",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.keuringsdatum",
                                       definition="Datum waarop het toestel laatst is gekeurd.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Datum waarop het toestel laatst is gekeurd."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlBrandblusserType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.type",
                                    definition="Het type van de brandblusser.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van de brandblusser."""
