# coding=utf-8
from OTLModel.Classes.Behuizing import Behuizing
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lokaal(Behuizing):
    """Een ruimte binnen een gebouw."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lokaal"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.grondplan = DtcDocument()
        """Plattegrond van het lokaal met aanduidingen van de verschillende aanwezige elementen zoals kasten met kastnummers, toegangscontrole en meer."""
        self.grondplan.naam = "grondplan"
        self.grondplan.label = "grondplan"
        self.grondplan.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lokaal.grondplan"
        self.grondplan.definition = "Plattegrond van het lokaal met aanduidingen van de verschillende aanwezige elementen zoals kasten met kastnummers, toegangscontrole en meer."
        self.grondplan.constraints = ""
        self.grondplan.usagenote = ""
        self.grondplan.deprecated_version = ""
