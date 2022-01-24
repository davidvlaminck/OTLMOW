# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class GroepMarkering(AIMObject):
    """Groepering om alle soorten markeringen te groeperen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepMarkering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._totaleGroepOppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                                    naam='totaleGroepOppervlakte',
                                                    label='totale oppervlakte groepering',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepMarkering.totaleGroepOppervlakte',
                                                    definition='De totale oppervlakte van de totale markering groepering.')

    @property
    def totaleGroepOppervlakte(self):
        """De totale oppervlakte van de totale markering groepering."""
        return self._totaleGroepOppervlakte.waarde

    @totaleGroepOppervlakte.setter
    def totaleGroepOppervlakte(self, value):
        self._totaleGroepOppervlakte.set_waarde(value, owner=self)
