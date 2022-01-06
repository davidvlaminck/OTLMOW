# coding=utf-8
from OTLModel.Classes.Buis import Buis
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlPersleidingMateriaal import KlPersleidingMateriaal
from OTLModel.Datatypes.KlSDRKlasse import KlSDRKlasse


# Generated with OTLClassCreator. To modify: extend, do not edit
class Persleiding(Buis):
    """Ondergronds kanaal of pijp voor afvoer van een vloeistof of gas onder druk."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlPersleidingMateriaal(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding.materiaal",
                                         definition="Bepaalt het materiaal van de persleiding.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Bepaalt het materiaal van de persleiding."""

        self.sdrKlasse = KeuzelijstField(naam="sdrKlasse",
                                         label="SDR klasse",
                                         lijst=KlSDRKlasse(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding.sdrKlasse",
                                         definition="De verhouding tussen de wanddikte en de diameter van de persleiding.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De verhouding tussen de wanddikte en de diameter van de persleiding."""
