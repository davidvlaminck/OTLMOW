# coding=utf-8
from OTLModel.Classes.Behuizing import Behuizing
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class Gebouw(Behuizing):
    """Elk bouwwerk, dat een voor mensen toegankelijke overdekte, geheel of gedeeltelijk met wanden omsloten ruimte vormt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.grondplan = DtcDocument()
        """Plattegrond van het gebouw met aanduidingen van de verschillende aanwezige elementen zoals kelder, kasten met kastnummers, toegangscontrole en meer."""
        self.grondplan.naam = "grondplan"
        self.grondplan.label = "grondplan"
        self.grondplan.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw.grondplan"
        self.grondplan.definition = "Plattegrond van het gebouw met aanduidingen van de verschillende aanwezige elementen zoals kelder, kasten met kastnummers, toegangscontrole en meer."
        self.grondplan.constraints = ""
        self.grondplan.usagenote = ""
        self.grondplan.deprecated_version = ""
