from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBouwputType import KlBouwputType
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bouwput(AIMObject):
    """De ontgraving die nodig is voor het maken van een ondergrondse constructie zoals bv. een put of putten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bouwput"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.putdiepte = KwantWrdInMeter()
        """Diepte tussen het maaiveld en onderkant bouwput in meter."""
        self.putdiepte.naam = "putdiepte"
        self.putdiepte.label = "putdiepte"
        self.putdiepte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bouwput.putdiepte"
        self.putdiepte.definition = "Diepte tussen het maaiveld en onderkant bouwput in meter."
        self.putdiepte.constraints = ""
        self.putdiepte.usagenote = ""
        self.putdiepte.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlBouwputType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bouwput.type",
                                    definition="Het type van bouwput.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van bouwput."""
