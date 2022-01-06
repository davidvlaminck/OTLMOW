from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefLuchtdichtheid(Proef):
    """Testen van de drukval van het beproefde leidingsvak."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuchtdichtheid"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.luchtdichtheid = DtcDocument()
        """Testresultaten van de opgemeten drukval van het beproefde leidingsvak."""
        self.luchtdichtheid.naam = "luchtdichtheid"
        self.luchtdichtheid.label = "luchtdichtheid"
        self.luchtdichtheid.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuchtdichtheid.luchtdichtheid"
        self.luchtdichtheid.definition = "Testresultaten van de opgemeten drukval van het beproefde leidingsvak."
        self.luchtdichtheid.constraints = ""
        self.luchtdichtheid.usagenote = ""
        self.luchtdichtheid.deprecated_version = ""
