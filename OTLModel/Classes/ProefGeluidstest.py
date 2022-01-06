# coding=utf-8
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcGeluidstestRapport import DtcGeluidstestRapport


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefGeluidstest(Proef):
    """Test van het geluidsscherm op oa. luchtgeluidsisolatie, geluidsabsorptie, e.d. """

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGeluidstest"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.geluidstestrapport = DtcGeluidstestRapport()
        """Het resultaat geluidstest."""
        self.geluidstestrapport.naam = "geluidstestrapport"
        self.geluidstestrapport.label = "geluidstestrapport"
        self.geluidstestrapport.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGeluidstest.geluidstestrapport"
        self.geluidstestrapport.definition = "Het resultaat geluidstest."
        self.geluidstestrapport.constraints = ""
        self.geluidstestrapport.usagenote = ""
        self.geluidstestrapport.deprecated_version = ""
