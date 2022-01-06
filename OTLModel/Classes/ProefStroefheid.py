# coding=utf-8
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefStroefheid(Proef):
    """Het vermogen van een wegdek om door voertuigbanden tangentieel uitgeoefende krachten (bij het nemen van bochten, afremmen of optrekken) te compenseren door even grote wrijvingskrachten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefStroefheid"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.stroefheid = DtcDocument()
        """Proefresultaten van de stroefheid."""
        self.stroefheid.naam = "stroefheid"
        self.stroefheid.label = "stroefheid"
        self.stroefheid.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefStroefheid.stroefheid"
        self.stroefheid.definition = "Proefresultaten van de stroefheid."
        self.stroefheid.constraints = ""
        self.stroefheid.usagenote = ""
        self.stroefheid.deprecated_version = ""
