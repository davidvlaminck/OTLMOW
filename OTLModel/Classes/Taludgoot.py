# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlTaludgootType import KlTaludgootType
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Taludgoot(AIMObject):
    """Goot die in het talud loodrecht op de kruinlijn is aangebracht. De functie hiervan is onder meer opvang en afvoer hemelwater."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taludgoot"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.totaleLengte = KwantWrdInMeter()
        """De totale lengte van de geprefabriceerde betonelementen in lopende meter vanaf het beginstuk (niet inbegrepen) tot aan het eindstuk (niet inbegrepen)."""
        self.totaleLengte.naam = "totaleLengte"
        self.totaleLengte.label = "totale lengte"
        self.totaleLengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taludgoot.totaleLengte"
        self.totaleLengte.definition = "De totale lengte van de geprefabriceerde betonelementen in lopende meter vanaf het beginstuk (niet inbegrepen) tot aan het eindstuk (niet inbegrepen)."
        self.totaleLengte.constraints = ""
        self.totaleLengte.usagenote = ""
        self.totaleLengte.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlTaludgootType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taludgoot.type",
                                    definition="Het type van geprefabriceerd betonelement.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van geprefabriceerd betonelement."""
