# coding=utf-8
from OTLModel.Classes.ConstructieElement import ConstructieElement
from OTLModel.Classes.BetonnenConstructieElement import BetonnenConstructieElement
from OTLModel.Classes.ConstructieElementenGC import ConstructieElementenGC
from OTLModel.Datatypes.DtcAfmetingBxlxhInCm import DtcAfmetingBxlxhInCm


# Generated with OTLClassCreator. To modify: extend, do not edit
class ConstructieSokkel(ConstructieElement, BetonnenConstructieElement, ConstructieElementenGC):
    """Betonnen zool die het object dat erop rust verhoogt of dat dient om een structuur op een goede manier te kunnen opleggen/verbinden met de fundering."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ConstructieSokkel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        ConstructieElement.__init__(self)
        BetonnenConstructieElement.__init__(self)
        ConstructieElementenGC.__init__(self)

        self.afmetingen = DtcAfmetingBxlxhInCm()
        """De afmetingen van de constructiesokkel."""
        self.afmetingen.naam = "afmetingen"
        self.afmetingen.label = "afmetingen"
        self.afmetingen.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ConstructieSokkel.afmetingen"
        self.afmetingen.definition = "De afmetingen van de constructiesokkel."
        self.afmetingen.constraints = ""
        self.afmetingen.usagenote = ""
        self.afmetingen.deprecated_version = ""
