# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlClusterClusterdoel import KlClusterClusterdoel


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cluster(AIMNaamObject):
    """Groep van servers die samenwerken om een gemeenschappelijk doel te bereiken (zowel voor groeperen van resources en/of redundantie)."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cluster"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.clusterdoel = KeuzelijstField(naam="clusterdoel",
                                           label="clusterdoel",
                                           lijst=KlClusterClusterdoel(),
                                           objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cluster.clusterdoel",
                                           definition="De reden waarom de custer is opgezet, bv. resources groeperen of redundantie.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """De reden waarom de custer is opgezet, bv. resources groeperen of redundantie."""
