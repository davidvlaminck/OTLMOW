# coding=utf-8
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWaterdichtheid(Proef):
    """Testen van het waterverlies van het beproefde leidingsvak."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWaterdichtheid"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.waterdichtheid = DtcDocument()
        """Testresultaten van het opgemeten waterverlies van het beproefde leidingsvak."""
        self.waterdichtheid.naam = "waterdichtheid"
        self.waterdichtheid.label = "waterdichtheid"
        self.waterdichtheid.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWaterdichtheid.waterdichtheid"
        self.waterdichtheid.definition = "Testresultaten van het opgemeten waterverlies van het beproefde leidingsvak."
        self.waterdichtheid.constraints = ""
        self.waterdichtheid.usagenote = ""
        self.waterdichtheid.deprecated_version = ""
