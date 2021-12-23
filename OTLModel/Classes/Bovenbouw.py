from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDekselKaderType import KlDekselKaderType
from OTLModel.Datatypes.KlDekselKlasse import KlDekselKlasse
from OTLModel.Datatypes.KlDekselMateriaal import KlDekselMateriaal
from OTLModel.Datatypes.KlDekselRegeling import KlDekselRegeling
from OTLModel.Datatypes.KlDekselVergrendeling import KlDekselVergrendeling
from OTLModel.Datatypes.KlRioleringVorm import KlRioleringVorm
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator
class Bovenbouw(AIMObject):
    """Een combinatie van het riooldeksel met de kader en de regeling."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
