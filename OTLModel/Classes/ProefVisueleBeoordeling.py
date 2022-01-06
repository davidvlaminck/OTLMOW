# coding=utf-8
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefVisueleBeoordeling(Proef):
    """Opsporen van de gebreken bij de definitieve oplevering."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVisueleBeoordeling"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.visueleBeoordeling = DtcDocument()
        """Een rapport van de visuele beoordeling van de laag."""
        self.visueleBeoordeling.naam = "visueleBeoordeling"
        self.visueleBeoordeling.label = "visuele beoordeling"
        self.visueleBeoordeling.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVisueleBeoordeling.visueleBeoordeling"
        self.visueleBeoordeling.definition = "Een rapport van de visuele beoordeling van de laag."
        self.visueleBeoordeling.constraints = ""
        self.visueleBeoordeling.usagenote = ""
        self.visueleBeoordeling.deprecated_version = ""
