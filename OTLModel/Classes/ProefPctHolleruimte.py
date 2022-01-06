from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefPctHolleruimte(Proef):
    """Proef om het percentage holle ruimte in een bitumineuze laag te bepalen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPctHolleruimte"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.pctHolleruimte = DtcDocument()
        """Het resultaat van het aantal percentage holleruimte meting aanwezig in de laag."""
        self.pctHolleruimte.naam = "pctHolleruimte"
        self.pctHolleruimte.label = "pct holleruimte"
        self.pctHolleruimte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPctHolleruimte.pctHolleruimte"
        self.pctHolleruimte.definition = "Het resultaat van het aantal percentage holleruimte meting aanwezig in de laag."
        self.pctHolleruimte.constraints = ""
        self.pctHolleruimte.usagenote = ""
        self.pctHolleruimte.deprecated_version = ""
