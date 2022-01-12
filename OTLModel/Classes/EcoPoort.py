# coding=utf-8
from OTLModel.Classes.ComplexeGeleiding import ComplexeGeleiding
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlEcoPoorttype import KlEcoPoorttype
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class EcoPoort(ComplexeGeleiding):
    """Een afsluitbare doorgang om mensen toe te laten tot het gebied."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EcoPoort"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.breedte = KwantWrdInMeter()
        """De breedte van de poort in meter."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EcoPoort.breedte"
        self.breedte.definition = "De breedte van de poort in meter."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""

        self.poortType = KeuzelijstField(naam="poortType",
                                         label="poort type",
                                         lijst=KlEcoPoorttype(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EcoPoort.poortType",
                                         definition="Bepaling van het type van poort.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Bepaling van het type van poort."""
