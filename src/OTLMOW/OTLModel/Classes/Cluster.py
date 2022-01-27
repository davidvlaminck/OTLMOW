# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from src.OTLMOW.OTLModel.Datatypes.KlClusterClusterdoel import KlClusterClusterdoel


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cluster(AIMNaamObject):
    """Groep van servers die samenwerken om een gemeenschappelijk doel te bereiken (zowel voor groeperen van resources en/of redundantie)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cluster'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._clusterdoel = OTLAttribuut(field=KlClusterClusterdoel,
                                         naam='clusterdoel',
                                         label='clusterdoel',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cluster.clusterdoel',
                                         definition='De reden waarom de custer is opgezet, bv. resources groeperen of redundantie.')

    @property
    def clusterdoel(self):
        """De reden waarom de custer is opgezet, bv. resources groeperen of redundantie."""
        return self._clusterdoel.waarde

    @clusterdoel.setter
    def clusterdoel(self, value):
        self._clusterdoel.set_waarde(value, owner=self)
