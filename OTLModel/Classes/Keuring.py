# coding=utf-8
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KwantWrdInJaar import KwantWrdInJaar


# Generated with OTLClassCreator. To modify: extend, do not edit
class Keuring:
    """Technische keuring uitgevoerd door een officiële keuringsinstantie."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#Keuring"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        self.datum = DateField(naam="datum",
                               label="keuringsdatum",
                               objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#Keuring.datum",
                               definition="De datum waarop de keuring werd uitgevoerd.",
                               constraints="",
                               usagenote="",
                               deprecated_version="")
        """De datum waarop de keuring werd uitgevoerd."""

        self.geldigheidsDuur = KwantWrdInJaar()
        """de periode (in jaar) waarbinnen de keuring geldig blijft. """
        self.geldigheidsDuur.naam = "geldigheidsDuur"
        self.geldigheidsDuur.label = "geldigheidsduur"
        self.geldigheidsDuur.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#Keuring.geldigheidsDuur"
        self.geldigheidsDuur.definition = "de periode (in jaar) waarbinnen de keuring geldig blijft. "
        self.geldigheidsDuur.constraints = ""
        self.geldigheidsDuur.usagenote = ""
        self.geldigheidsDuur.deprecated_version = ""

        self.verslag = DtcDocument()
        """document met het verslag van de keuring."""
        self.verslag.naam = "verslag"
        self.verslag.label = "keuringsverslag"
        self.verslag.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#Keuring.verslag"
        self.verslag.definition = "document met het verslag van de keuring."
        self.verslag.constraints = ""
        self.verslag.usagenote = ""
        self.verslag.deprecated_version = ""
