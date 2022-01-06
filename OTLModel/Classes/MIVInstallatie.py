from OTLModel.Classes.NaampadObject import NaampadObject
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class MIVInstallatie(NaampadObject):
    """De volledige opstelling voor meten in Vlaanderen op een bepaalde locatie."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.lusConfig = DtcDocument()
        """Een definierende tabel die relatie legt tussen meetpuntnummer lusvolgorde nummer en de GPS locatie."""
        self.lusConfig.naam = "lusConfig"
        self.lusConfig.label = "lus config"
        self.lusConfig.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie.lusConfig"
        self.lusConfig.definition = "Een definierende tabel die relatie legt tussen meetpuntnummer lusvolgorde nummer en de GPS locatie."
        self.lusConfig.constraints = ""
        self.lusConfig.usagenote = "Bestanden van het type xlsx."
        self.lusConfig.deprecated_version = ""

        self.technischeDocumentatie = DtcDocument()
        """Documentatie van de onderdelen: LVE / luskaart / communicatiekaart, configurator,  ..."""
        self.technischeDocumentatie.naam = "technischeDocumentatie"
        self.technischeDocumentatie.label = "technische documentatie"
        self.technischeDocumentatie.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie.technischeDocumentatie"
        self.technischeDocumentatie.definition = "Documentatie van de onderdelen: LVE / luskaart / communicatiekaart, configurator,  ..."
        self.technischeDocumentatie.constraints = ""
        self.technischeDocumentatie.usagenote = "Bestanden van het type pdf."
        self.technischeDocumentatie.deprecated_version = ""
