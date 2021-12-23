from OTLModel.Classes.SoftwareToegang import SoftwareToegang
from OTLModel.Datatypes.DtcSoftwarePoortconfiguratie import DtcSoftwarePoortconfiguratie


# Generated with OTLClassCreator
class LogischePoort(SoftwareToegang):
    """Een 'logische' connectie waaraan een nummer tussen 0 en 65536 wordt toegewezen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LogischePoort"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.poortconfiguratie = DtcSoftwarePoortconfiguratie()
        """Type TCP of UDP service."""
        self.poortconfiguratie.naam = "poortconfiguratie"
        self.poortconfiguratie.label = "poortconfiguratie"
        self.poortconfiguratie.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LogischePoort.poortconfiguratie"
        self.poortconfiguratie.definition = "Type TCP of UDP service."
        self.poortconfiguratie.constraints = ""
        self.poortconfiguratie.usagenote = ""
        self.poortconfiguratie.deprecated_version = ""
