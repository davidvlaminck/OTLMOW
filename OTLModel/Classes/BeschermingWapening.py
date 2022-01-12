# coding=utf-8
from OTLModel.Classes.AndereLaag import AndereLaag
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBeschermingWapeningType import KlBeschermingWapeningType


# Generated with OTLClassCreator. To modify: extend, do not edit
class BeschermingWapening(AndereLaag):
    """De bescherming of de wapening van de onderfundering, fundering of grondmassief."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BeschermingWapening"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlBeschermingWapeningType(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BeschermingWapening.type",
                                    definition="Het type bescherming of wapening.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type bescherming of wapening."""
