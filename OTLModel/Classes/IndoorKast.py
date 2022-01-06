from OTLModel.Classes.Kast import Kast
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class IndoorKast(Kast):
    """Behuizing in de vorm van een kast voor gebruik in binnenruimtes."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IndoorKast"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        mplanField = DtcDocument()
        mplanField.naam = "mplan"
        mplanField.label = "m-plan"
        mplanField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IndoorKast.mplan"
        mplanField.definition = "Mechanisch plan van de volledige installatie. Er wordt 1 plan toegevoegd per installatie/techniek die op de kast is aangesloten."
        mplanField.constraints = ""
        mplanField.usagenote = "Bestanden van het type dwg of pdf."
        mplanField.deprecated_version = ""
        self.mplan = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=mplanField)
        """Mechanisch plan van de volledige installatie. Er wordt 1 plan toegevoegd per installatie/techniek die op de kast is aangesloten."""
