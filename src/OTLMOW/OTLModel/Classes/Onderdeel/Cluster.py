# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.KlClusterClusterdoel import KlClusterClusterdoel
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cluster(AIMNaamObject, PuntGeometrie):
    """Groep van servers die samenwerken om een gemeenschappelijk doel te bereiken (zowel voor groeperen van resources en/of redundantie)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cluster'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VirtueleServer')

        self._clusterdoel = OTLAttribuut(field=KlClusterClusterdoel,
                                         naam='clusterdoel',
                                         label='clusterdoel',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cluster.clusterdoel',
                                         definition='De reden waarom de custer is opgezet, bv. resources groeperen of redundantie.',
                                         owner=self)

    @property
    def clusterdoel(self):
        """De reden waarom de custer is opgezet, bv. resources groeperen of redundantie."""
        return self._clusterdoel.get_waarde()

    @clusterdoel.setter
    def clusterdoel(self, value):
        self._clusterdoel.set_waarde(value, owner=self)
