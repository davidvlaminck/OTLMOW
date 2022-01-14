# coding=utf-8
from OTLModel.Classes.ContainerBuis import ContainerBuis
from OTLModel.Classes.Buis import Buis
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlRioleringsbuisMateriaal import KlRioleringsbuisMateriaal


# Generated with OTLClassCreator. To modify: extend, do not edit
class Mantelbuis(ContainerBuis, Buis):
    """Een ondergrondse buis bestemd voor de doorvoer van kabels en/of leidingen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Mantelbuis"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Buis.__init__(self)
        ContainerBuis.__init__(self)

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlRioleringsbuisMateriaal(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Mantelbuis.materiaal",
                                         definition="Bepaalt het materiaal van de mantelbuis.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Bepaalt het materiaal van de mantelbuis."""
