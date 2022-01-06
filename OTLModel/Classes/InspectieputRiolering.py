# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Classes.Put import Put
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlPutType import KlPutType
from OTLModel.Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden


# Generated with OTLClassCreator. To modify: extend, do not edit
class InspectieputRiolering(AIMObject, Put):
    """Dient om de aanwezige riolering te kunnen inspecteren, reinigen of onderhouden. """

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#InspectieputRiolering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        Put.__init__(self)

        self.hoekverdraaiing = KwantWrdInDecimaleGraden()
        """Verschil in richting tussen inkomende en uitgaande rioolbuis."""
        self.hoekverdraaiing.naam = "hoekverdraaiing"
        self.hoekverdraaiing.label = "hoekverdraaiing"
        self.hoekverdraaiing.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#InspectieputRiolering.hoekverdraaiing"
        self.hoekverdraaiing.definition = "Verschil in richting tussen inkomende en uitgaande rioolbuis."
        self.hoekverdraaiing.constraints = ""
        self.hoekverdraaiing.usagenote = ""
        self.hoekverdraaiing.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlPutType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#InspectieputRiolering.type",
                                    definition="Het type van de put zoals beschreven in hoofdstuk 7 van het standaardbestek 250.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van de put zoals beschreven in hoofdstuk 7 van het standaardbestek 250."""
