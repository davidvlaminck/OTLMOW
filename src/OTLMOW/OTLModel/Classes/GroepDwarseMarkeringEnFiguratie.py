# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class GroepDwarseMarkeringEnFiguratie(AIMObject, PuntGeometrie):
    """Groepering van de dwarse- en figuratiemarkering."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepDwarseMarkeringEnFiguratie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._totaleOppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                               naam='totaleOppervlakte',
                                               label='totale oppervlakte',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepDwarseMarkeringEnFiguratie.totaleOppervlakte',
                                               definition='De oppervlakte van de groep dwarse en/of figuratie markering.',
                                               owner=self)

        self._tussenruimte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='tussenruimte',
                                          label='tussenruimte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepDwarseMarkeringEnFiguratie.tussenruimte',
                                          definition='De lengte van de tussenruimte in meter tussen de dwarse en/of figuratie markering.',
                                          owner=self)

    @property
    def totaleOppervlakte(self):
        """De oppervlakte van de groep dwarse en/of figuratie markering."""
        return self._totaleOppervlakte.waarde

    @totaleOppervlakte.setter
    def totaleOppervlakte(self, value):
        self._totaleOppervlakte.set_waarde(value, owner=self)

    @property
    def tussenruimte(self):
        """De lengte van de tussenruimte in meter tussen de dwarse en/of figuratie markering."""
        return self._tussenruimte.waarde

    @tussenruimte.setter
    def tussenruimte(self, value):
        self._tussenruimte.set_waarde(value, owner=self)
