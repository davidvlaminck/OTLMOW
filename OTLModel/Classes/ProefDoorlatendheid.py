# coding=utf-8
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefDoorlatendheid(Proef):
    """De controle van de doorlatendheid van het oppervlak met behulp van de dubbele ringmethode."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDoorlatendheid"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.doorlatendheid = DtcDocument()
        """Proefresultaten van de waterdoorlatendheid."""
        self.doorlatendheid.naam = "doorlatendheid"
        self.doorlatendheid.label = "doorlatendheid"
        self.doorlatendheid.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDoorlatendheid.doorlatendheid"
        self.doorlatendheid.definition = "Proefresultaten van de waterdoorlatendheid."
        self.doorlatendheid.constraints = ""
        self.doorlatendheid.usagenote = ""
        self.doorlatendheid.deprecated_version = ""
