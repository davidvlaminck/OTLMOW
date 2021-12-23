from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator
class GroepDwarseMarkeringEnFiguratie(AIMObject):
    """Groepering van de dwarse- en figuratiemarkering."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepDwarseMarkeringEnFiguratie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.totaleOppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte van de groep dwarse en/of figuratie markering."""
        self.totaleOppervlakte.naam = "totaleOppervlakte"
        self.totaleOppervlakte.label = "totale oppervlakte"
        self.totaleOppervlakte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepDwarseMarkeringEnFiguratie.totaleOppervlakte"
        self.totaleOppervlakte.definition = "De oppervlakte van de groep dwarse en/of figuratie markering."
        self.totaleOppervlakte.constraints = ""
        self.totaleOppervlakte.usagenote = ""
        self.totaleOppervlakte.deprecated_version = ""

        self.tussenruimte = KwantWrdInMeter()
        """De lengte van de tussenruimte in meter tussen de dwarse en/of figuratie markering."""
        self.tussenruimte.naam = "tussenruimte"
        self.tussenruimte.label = "tussenruimte"
        self.tussenruimte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepDwarseMarkeringEnFiguratie.tussenruimte"
        self.tussenruimte.definition = "De lengte van de tussenruimte in meter tussen de dwarse en/of figuratie markering."
        self.tussenruimte.constraints = ""
        self.tussenruimte.usagenote = ""
        self.tussenruimte.deprecated_version = ""
