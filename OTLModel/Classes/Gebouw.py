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

        self.waarde.grondplan = DtcDocument()
        """Plattegrond van het gebouw met aanduidingen van de verschillende aanwezige elementen zoals kelder, kasten met kastnummers, toegangscontrole en meer."""
        self.waarde.grondplan.naam = "grondplan"
        self.waarde.grondplan.label = "grondplan"
        self.waarde.grondplan.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw.grondplan"
        self.waarde.grondplan.definition = "Plattegrond van het gebouw met aanduidingen van de verschillende aanwezige elementen zoals kelder, kasten met kastnummers, toegangscontrole en meer."
        self.waarde.grondplan.constraints = ""
        self.waarde.grondplan.usagenote = ""
        self.waarde.grondplan.deprecated_version = ""
        self.grondplan = self.waarde.grondplan
