from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlWegdekvoegType import KlWegdekvoegType
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator
class Wegdekvoeg(AIMObject):
    """Dwarsvoegen en langsvoegen met uitzondering van de krimpvoegen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.heeftDeuvels = BooleanField(naam="heeftDeuvels",
                                         label="heeft deuvels",
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg.heeftDeuvels",
                                         definition="Aanduiding of de voeg al dan niet verdeuveld is.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Aanduiding of de voeg al dan niet verdeuveld is."""

        self.lengte = KwantWrdInMeter()
        """De lengte van de wegdekvoeg."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg.lengte"
        self.lengte.definition = "De lengte van de wegdekvoeg."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlWegdekvoegType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg.type",
                                    definition="Het type van wegdekvoeg.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van wegdekvoeg."""
