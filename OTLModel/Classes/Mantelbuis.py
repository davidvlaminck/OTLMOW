# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.ContainerBuis import ContainerBuis
from OTLModel.Classes.Buis import Buis
from OTLModel.Datatypes.KlRioleringsbuisMateriaal import KlRioleringsbuisMateriaal


# Generated with OTLClassCreator. To modify: extend, do not edit
class Mantelbuis(ContainerBuis, Buis, AttributeInfo):
    """Een ondergrondse buis bestemd voor de doorvoer van kabels en/of leidingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Mantelbuis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Buis.__init__(self)
        ContainerBuis.__init__(self)

        self._materiaal = OTLAttribuut(field=KlRioleringsbuisMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Mantelbuis.materiaal',
                                       definition='Bepaalt het materiaal van de mantelbuis.')

    @property
    def materiaal(self):
        """Bepaalt het materiaal van de mantelbuis."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
