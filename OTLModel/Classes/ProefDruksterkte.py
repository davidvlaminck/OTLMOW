# coding=utf-8
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefDruksterkte(Proef):
    """De spanning waarbij het materiaal van de laag onder invloed van (druk)belasting bezwijkt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDruksterkte"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.druksterkte = DtcDocument()
        """Proefresultaten van de druksterkte van de laag."""
        self.druksterkte.naam = "druksterkte"
        self.druksterkte.label = "druksterkte"
        self.druksterkte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDruksterkte.druksterkte"
        self.druksterkte.definition = "Proefresultaten van de druksterkte van de laag."
        self.druksterkte.constraints = ""
        self.druksterkte.usagenote = ""
        self.druksterkte.deprecated_version = ""
