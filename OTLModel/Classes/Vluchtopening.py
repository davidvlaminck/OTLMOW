# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEGCOpeningType import KlLEGCOpeningType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Vluchtopening(AIMObject):
    """Vluchtopeningen voorzien een vluchtmogelijkheid. Deze bezitten dezelfde akoestische kwaliteitseisen als de voorgestelde schermen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vluchtopening"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.technischeFiche = DtcDocument()
        """Document waarin onder andere het inplantingsplan van de doorgang wordt weergegeven."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vluchtopening.technischeFiche"
        self.technischeFiche.definition = "Document waarin onder andere het inplantingsplan van de doorgang wordt weergegeven."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""
