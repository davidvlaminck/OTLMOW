# coding=utf-8
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefVerankeringskracht(Proef):
    """Een trekproef in situ om de verankering van de ankerstaven in een betonverharding te testen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVerankeringskracht"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.verankeringskracht = DtcDocument()
        """Het resultaat van de test om de verankeringskracht in de BV laag."""
        self.verankeringskracht.naam = "verankeringskracht"
        self.verankeringskracht.label = "verankeringskracht"
        self.verankeringskracht.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVerankeringskracht.verankeringskracht"
        self.verankeringskracht.definition = "Het resultaat van de test om de verankeringskracht in de BV laag."
        self.verankeringskracht.constraints = ""
        self.verankeringskracht.usagenote = ""
        self.verankeringskracht.deprecated_version = ""