from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Classes.BevestigingGC import BevestigingGC
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBevestigingsbeugelType import KlBevestigingsbeugelType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bevestigingsbeugel(AIMNaamObject, BevestigingGC):
    """Verbindingsstuk waarmee een object kan vastgemaakt worden aan een steun of oppervlak."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        BevestigingGC.__init__(self)

        berekeningsnotaField = DtcDocument()
        berekeningsnotaField.naam = "berekeningsnota"
        berekeningsnotaField.label = "berekeningsnota"
        berekeningsnotaField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel.berekeningsnota"
        berekeningsnotaField.definition = "Document met de berekeningsnota van de bevestigingsbeugel."
        berekeningsnotaField.constraints = ""
        berekeningsnotaField.usagenote = "Bestanden van het type xlsx of pdf."
        berekeningsnotaField.deprecated_version = ""
        self.berekeningsnota = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=berekeningsnotaField)
        """Document met de berekeningsnota van de bevestigingsbeugel."""

        constructieEnMontageplanField = DtcDocument()
        constructieEnMontageplanField.naam = "constructieEnMontageplan"
        constructieEnMontageplanField.label = "constructie en montageplan"
        constructieEnMontageplanField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel.constructieEnMontageplan"
        constructieEnMontageplanField.definition = "Document met het constructie- en montageplan van de bevestigingsbeugel."
        constructieEnMontageplanField.constraints = ""
        constructieEnMontageplanField.usagenote = "Bestanden van het type dwg of pdf."
        constructieEnMontageplanField.deprecated_version = ""
        self.constructieEnMontageplan = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=constructieEnMontageplanField)
        """Document met het constructie- en montageplan van de bevestigingsbeugel."""

        self.isVerzegeld = BooleanField(naam="isVerzegeld",
                                        label="is verzegeld",
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel.isVerzegeld",
                                        definition="Geeft aan of de bevestigingsbeugel verzegeld is tegen het ongemerkt losmaken ervan.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Geeft aan of de bevestigingsbeugel verzegeld is tegen het ongemerkt losmaken ervan."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlBevestigingsbeugelType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel.type",
                                    definition="Het type van de bevestigingsbeugel.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van de bevestigingsbeugel."""
