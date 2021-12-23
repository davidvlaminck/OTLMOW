from OTLModel.Classes.LinkendElement import LinkendElement
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAansluitstukMateriaal import KlAansluitstukMateriaal
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator
class Aansluitmof(LinkendElement):
    """Aansluitingsstuk tussen 2 buizen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitmof"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.diameter = KwantWrdInMillimeter()
        """De diameter van het boorgat gebruikt door de aansluitmof  in millimeter."""
        self.diameter.naam = "diameter"
        self.diameter.label = "diameter"
        self.diameter.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitmof.diameter"
        self.diameter.definition = "De diameter van het boorgat gebruikt door de aansluitmof  in millimeter."
        self.diameter.constraints = ""
        self.diameter.usagenote = ""
        self.diameter.deprecated_version = ""

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlAansluitstukMateriaal(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitmof.materiaal",
                                         definition="Het materiaal van de aansluitmof.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Het materiaal van de aansluitmof."""
