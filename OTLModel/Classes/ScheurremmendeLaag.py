# coding=utf-8
from OTLModel.Classes.AndereLaag import AndereLaag
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlScheurremmendeLaagType import KlScheurremmendeLaagType


# Generated with OTLClassCreator. To modify: extend, do not edit
class ScheurremmendeLaag(AndereLaag):
    """Een scheurremmende laag is een laag onder andere bitumineuze lagen om reflectiescheurvorming tegen te gaan of een wegstructuur te versterken (asfaltwapening)."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ScheurremmendeLaag"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlScheurremmendeLaagType(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ScheurremmendeLaag.type",
                                    definition="Het type scheurremmende laag.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type scheurremmende laag."""
