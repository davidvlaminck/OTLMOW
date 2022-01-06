# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class GroepMarkering(AIMObject):
    """Groepering om alle soorten markeringen te groeperen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepMarkering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.totaleGroepOppervlakte = KwantWrdInVierkanteMeter()
        """De totale oppervlakte van de totale markering groepering."""
        self.totaleGroepOppervlakte.naam = "totaleGroepOppervlakte"
        self.totaleGroepOppervlakte.label = "totale oppervlakte groepering"
        self.totaleGroepOppervlakte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepMarkering.totaleGroepOppervlakte"
        self.totaleGroepOppervlakte.definition = "De totale oppervlakte van de totale markering groepering."
        self.totaleGroepOppervlakte.constraints = ""
        self.totaleGroepOppervlakte.usagenote = ""
        self.totaleGroepOppervlakte.deprecated_version = ""
